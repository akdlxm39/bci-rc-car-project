"""
분류 모델 정의 및 로딩/추론 유틸리티.

- MLP 모델 구조 정의
- load_model(...): 동기 방식 모델 로더
- async_predict(...): 추론을 스레드로 넘겨 비동기 루프를 막지 않는 래퍼
"""

import torch
import torch.nn as nn
import numpy as np
import asyncio
from torch.nn.functional import softmax


class MLP(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, min_value, max_value):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)  # 입력층 -> 은닉층
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.relu2 = nn.ReLU()
        self.fc3 = nn.Linear(hidden_size, output_size)  # 은닉층 -> 출력층

        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x):
        x = self.preprocess(x)
        x = self.fc1(x)
        x = self.relu1(x)
        x = self.fc3(x)
        return x

    def preprocess(self, feature):
        feature = np.array(feature, dtype=np.float32)
        input_tensor = torch.from_numpy(feature).unsqueeze(0)
        normalized_input_tensor = 2 * (input_tensor - self.min_value) / (self.max_value - self.min_value) - 1
        return normalized_input_tensor

def load_model(model_path, norm_params_path, input_size=None, hidden_size=None, output_size=None, map_location=None):
    """MLP 인스턴스를 만들고 가중치를 로드한다.

    input_size / hidden_size / output_size가 비어 있으면
    체크포인트에서 구조 정보를 유추하려고 시도한다.
    """
    if input_size is None or hidden_size is None or output_size is None:
        # 가능한 범위에서 state_dict를 읽어 차원을 추정한다.
        state = torch.load(model_path, map_location=map_location)
        # 차원을 정확히 유추하기 어려우면 기본값으로 보정한다.
        if isinstance(state, dict):
            input_size = input_size or 20
            hidden_size = hidden_size or 16
            output_size = output_size or 4
    norm_params = torch.load(norm_params_path, map_location=map_location)
    model = MLP(input_size, hidden_size, output_size, norm_params['min_val'], norm_params['max_val'])
    try:
        model.load_state_dict(torch.load(model_path, map_location=map_location))
    except Exception:
        # 체크포인트가 dict 형태일 경우 model_state_dict 키를 우선 시도한다.
        try:
            ckpt = torch.load(model_path, map_location=map_location)
            model.load_state_dict(ckpt.get('model_state_dict', ckpt))
        except Exception as e:
            print(f"[model.load_model] 경고: 가중치를 불러오지 못했습니다: {e}")
    model.eval()
    return model

async def async_predict(model, input_tensor, device=None):
    """이벤트 루프를 막지 않도록 모델 추론을 스레드에서 실행한다."""
    if device is None:
        device = next(model.parameters()).device if any(True for _ in model.parameters()) else torch.device('cpu')
    # 올바른 디바이스와 배치 차원을 보장한다.
    def _run():
        model.to(device)
        model.eval()
        with torch.no_grad():
            t = input_tensor
            if not isinstance(t, torch.Tensor):
                t = torch.tensor(t, dtype=torch.float32)
            if t.dim() == 1:
                t = t.unsqueeze(0)
            t = t.to(device)
            out = model(t)
            out = softmax(out, dim=-1)
            out = out.squeeze()
            return out.cpu()
    return await asyncio.to_thread(_run)
