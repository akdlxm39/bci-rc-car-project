"""
LSL 스트림 비동기 래퍼.

- pylsl의 blocking 호출을 asyncio.to_thread로 감싼다.
- connect_stream(...)은 StreamInlet을 반환한다.
- read_sample(...)은 (sample, timestamp)를 반환한다.
"""

from pylsl import StreamInlet, resolve_byprop
import asyncio

async def resolve_stream(type_name="EEG", timeout=5.0):
    """이벤트 루프를 막지 않도록 스레드에서 LSL 스트림을 탐색한다."""
    def _resolve():
        return resolve_byprop('type', type_name, timeout=timeout)
    streams = await asyncio.to_thread(_resolve)
    return streams

async def connect_stream(type_name='EEG', timeout=5.0):
    streams = await resolve_stream(type_name, timeout=timeout)
    if not streams:
        raise RuntimeError(f"type={type_name} 인 LSL 스트림을 찾지 못했습니다.")
    inlet = StreamInlet(streams[0])
    return inlet

async def read_sample(inlet, timeout=1.0):
    """to_thread를 사용해 샘플을 읽는다. timeout이면 (None, None)을 반환한다."""
    def _pull():
        return inlet.pull_sample(timeout=timeout)
    sample, timestamp = await asyncio.to_thread(_pull)
    return sample, timestamp
