"""
arduino_io.py
- Async Arduino connection and send helper.
- Prefer serial_asyncio if available; otherwise use a simple thread-based writer with pyserial.
"""

import sys, asyncio
from bleak import BleakClient, BleakScanner, BleakError

SERVICE_UUID = "0000ffe0-0000-1000-8000-00805f9b34fb"
CHAR_UUID    = "0000ffe1-0000-1000-8000-00805f9b34fb"
TARGET_NAME = "HMSoft"
TARGET_ADDR = None
APPEND_NEWLINE = False  # 아두이노가 개행 필요하면 True로 변경


def handle_notify(_, data: bytearray):
    try:
        print(f"\n[HM-10→PC] {data.decode('utf-8', errors='ignore')}", end="")
    except Exception:
        print(f"\n[HM-10→PC RAW] {data}")

async def _choose_write_response(client) -> bool:
    """
    서비스 디스커버리 후 characteristic properties를 보고 write 모드 결정.
    (get_services 경고 제거: client.services 사용)
    """
    ch = client.services.get_characteristic(CHAR_UUID)
    if not ch:
        # characteristic을 못 찾으면 안전하게 response=True
        return True
    props = set(ch.properties or [])
    if "write-without-response" in props and "write" not in props:
        return False
    if "write" in props and "write-without-response" not in props:
        return True
    return True if sys.platform == "darwin" else False

def _chunk_bytes(b: bytes, n: int = 20):
    for i in range(0, len(b), n):
        yield b[i:i+n]


async def connect_arduino():
    device = None
    if TARGET_ADDR:
        print(f"주소로 연결 시도: {TARGET_ADDR}")
        device = TARGET_ADDR
    else:
        print(f"스캔 중... (이름: {TARGET_NAME})")
        devices = await BleakScanner.discover(timeout=5.0)

        for d in devices:
            if (d.name or "").strip() == TARGET_NAME:
                device = d
                break
        if not device:
            raise RuntimeError("{TARGET_NAME}을 찾지 못했습니다. 이름/주소를 확인하세요.")
            return
    client = BleakClient(device)
    await client.connect()

    await asyncio.sleep(0.2)
    services = client.services
    char = services.get_characteristic(CHAR_UUID)
    return client, char

async def push_char(client, port, message):
    await client.start_notify(port, handle_notify)
    use_response = await _choose_write_response(client)
    payload = (message[0] + ("\n" if APPEND_NEWLINE else "")).encode("utf-8")
    try:
        for part in _chunk_bytes(payload, 20):
            await client.write_gatt_char(port, part, response=use_response)
            await asyncio.sleep(0.01)
    finally:
        try:
            await client.stop_notify(port)
        except Exception:
            pass