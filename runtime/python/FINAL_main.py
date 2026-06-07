"""
main.py
- Example top-level async runner that ties LSL -> preprocess -> model -> Arduino
- Collects 3 seconds of data (256 Hz × 3 = 768 samples) and predicts using the average.
"""

import asyncio
import time
from pathlib import Path

import numpy as np
from numpy.f2py.auxfuncs import throw_error

from model import load_model, async_predict
from signal_utils import filtering_sample, create_filter, normalize_signal
from lsl_stream import connect_stream, read_sample
from arduino_io import connect_arduino, push_char

# --- Configuration ---
PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = PROJECT_ROOT / "models" / "FINAL_raw_data_model.pth"
NORM_PARAMS_PATH = PROJECT_ROOT / "models" / "FINAL_normalization_params.pth"
MODEL_IN = 20
MODEL_HID = 16
MODEL_OUT = 4
ARDUINO_BAUD = 9600

FS = 256     # Hz (samples per second)
DURATION = 3 # seconds
WINDOW_SIZE = FS * DURATION  # 768 samples
PRED_DURATION = 1 # seconds
PRED_WINDOW_SIZE = FS * PRED_DURATION # samples
msg_dict = {0:'L', 1 : 'R', 2 :'S', 3:'S'}
labels = ('Left', 'Right', 'Forward', 'Forward')

async def worker(inlet, model, arduino, port, filter, state):
    buffer = np.zeros((20, WINDOW_SIZE))  # stores incoming samples
    cur = 0
    start_time = time.time()
    await push_char(arduino, port, 'a')
    while True:
        sample, ts = await read_sample(inlet, timeout=1.0)

        if sample is None:
            await asyncio.sleep(0.01)
            continue
        try:
            # LSL sample to numpy array
            raw = np.asarray(sample)
            filtering_sample(raw, filter, state, buffer, cur)
            cur += 1
            if cur % PRED_WINDOW_SIZE == 0:
                x = normalize_signal(buffer)
                out = await async_predict(model, x)
                # Convert to label
                label = int(out.argmax(dim=-1).item()) if hasattr(out, "argmax") else int(np.argmax(out))
                msg = f"{msg_dict[label]}\n"
                # Send to Arduino
                await push_char(arduino, port, msg)

                current_time = time.time() - start_time

                print(f"{labels[label]:<10} {out[label]*100:6.2f}% {current_time:6.0f}s")


            if cur >= WINDOW_SIZE: cur = 0

        except Exception as e:
            print(f"[worker] error processing block: {e}")
            await push_char(arduino, port, 'z')
            await asyncio.sleep(0.05)
            return

#
# async def test(arduino, port):
#     start_time = time.time()
#     await push_char(arduino, port, 'A')
#     for c in string:
#         await asyncio.sleep(1)
#         cur_time = time.time() - start_time
#         await push_char(arduino, port, c)
#         print(f"cur_time : {cur_time:6.0f}, msg : {c}")
#     await push_char(arduino, port, 'Z')


async def main():
    print("Loading model...")
    model = load_model(MODEL_PATH, NORM_PARAMS_PATH, input_size=MODEL_IN, hidden_size=MODEL_HID, output_size=MODEL_OUT, map_location="cpu")

    print("Connecting to LSL...")
    inlet = await connect_stream("EEG", timeout=5.0)
    print("Connected to LSL stream.")
    # inlet = None

    print("Connecting to Arduino...")
    arduino, port = await connect_arduino()
    print("Connected to Arduino.")
    # arduino, port = None, None

    filter, state = create_filter(FS)

    print(f"Collecting {DURATION}s windows ({WINDOW_SIZE} samples per prediction)...")
    try:
        await worker(inlet, model, arduino, port, filter, state)
    except KeyboardInterrupt:
        await push_char(arduino, port, 'z')
        raise KeyboardInterrupt
    except RuntimeError as e:
        print(e)

    # await test(arduino, port)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:

        print("Interrupted by user.")
