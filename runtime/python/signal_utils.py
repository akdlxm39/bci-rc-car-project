"""
신호 전처리 유틸리티.

- 필터링
- 정규화
- 실시간 입력을 모델 입력 형태로 변환하는 보조 함수
"""

import numpy as np
from scipy.signal import cheby1, sosfilt

def filter_sample_with_state(sample, sos, state):
    y, new_state = sosfilt(sos, [sample], zi=state)
    return y[0], new_state

def create_filter(sample_freq):
    iir_filters = [cheby1(4, 0.5, cutoff, btype='bandpass', fs=sample_freq, output='sos')
                   for _ in range(4) for cutoff in [[8, 12], [12, 20], [20, 30], [30, 35], [35, 40]]]
    filter_states = [np.zeros((sos.shape[0], 2)) for sos in iir_filters]
    return iir_filters, filter_states

def normalize_signal(x, eps=1e-8):
    x = np.power(x, 2)
    x = np.mean(x, axis=1).flatten()
    x = np.log(x + eps)
    return x

def filtering_sample(raw_sample, iir_filters, filter_states, filtered_eeg, x):
    """고수준 전처리 함수.

    - 대역통과 필터 적용
    - 채널/대역별 출력을 버퍼에 저장
    - 이후 정규화 시 사용할 입력 형태를 유지
    """
    for i in range(20):
        filtered_sample, new_state = filter_sample_with_state(raw_sample[i % 4], iir_filters[i], filter_states[i])
        filter_states[i] = new_state
        filtered_eeg[i, x] = filtered_sample
