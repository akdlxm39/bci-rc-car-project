"""
lsl_stream.py
- Async wrappers to read from pylsl (which is blocking) using asyncio.to_thread.
- connect_stream(type_name='EEG') -> returns StreamInlet
- read_sample(inlet, timeout=1.0) -> returns (sample, timestamp)
"""

from pylsl import StreamInlet, resolve_byprop
import asyncio

async def resolve_stream(type_name="EEG", timeout=5.0):
    """Resolve streams by property in a thread to avoid blocking the event loop."""
    def _resolve():
        return resolve_byprop('type', type_name, timeout=timeout)
    streams = await asyncio.to_thread(_resolve)
    return streams

async def connect_stream(type_name='EEG', timeout=5.0):
    streams = await resolve_stream(type_name, timeout=timeout)
    if not streams:
        raise RuntimeError(f"No LSL stream found with type={type_name}")
    inlet = StreamInlet(streams[0])
    return inlet

async def read_sample(inlet, timeout=1.0):
    """Pull a sample using to_thread. Returns (sample, timestamp) or (None, None) if timeout"""
    def _pull():
        return inlet.pull_sample(timeout=timeout)
    sample, timestamp = await asyncio.to_thread(_pull)
    return sample, timestamp
