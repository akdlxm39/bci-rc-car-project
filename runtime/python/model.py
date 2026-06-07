"""
model.py
- MLP definition
- load_model(model_path, ...) : synchronous loader
- async_predict(model, input_tensor) : asynchronous wrapper for inference
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
        # x = self.fc2(x)
        # x = self.relu2(x)
        x = self.fc3(x)
        return x

    def preprocess(self, feature):
        feature = np.array(feature, dtype=np.float32)
        input_tensor = torch.from_numpy(feature).unsqueeze(0)
        normalized_input_tensor = 2 * (input_tensor - self.min_value) / (self.max_value - self.min_value) - 1
        return normalized_input_tensor

def load_model(model_path, norm_params_path, input_size=None, hidden_size=None, output_size=None, map_location=None):
    """Create an MLP instance and load state_dict if provided.
    If input_size/hidden_size/output_size are None, try to load a full checkpoint
    that contains 'arch' info. This loader is conservative and simple.
    """
    if input_size is None or hidden_size is None or output_size is None:
        # Try to load state dict to infer sizes (best-effort)
        state = torch.load(model_path, map_location=map_location)
        # If state is a state_dict, we cannot easily infer dims; user should pass dims.
        # Fall back to a small default
        if isinstance(state, dict):
            input_size = input_size or 20
            hidden_size = hidden_size or 16
            output_size = output_size or 4
    norm_params = torch.load(norm_params_path, map_location=map_location)
    model = MLP(input_size, hidden_size, output_size, norm_params['min_val'], norm_params['max_val'])
    print("check 1")
    try:
        model.load_state_dict(torch.load(model_path, map_location=map_location))
        print("check 2")
    except Exception:
        # Maybe checkpoint is a dict with key 'model_state_dict'
        try:
            ckpt = torch.load(model_path, map_location=map_location)
            model.load_state_dict(ckpt.get('model_state_dict', ckpt))
        except Exception as e:
            print(f"[model.load_model] Warning: couldn't load weights: {e}")
    model.eval()
    return model

async def async_predict(model, input_tensor, device=None):
    """Run model inference without blocking the event loop by offloading to a thread."""
    if device is None:
        device = next(model.parameters()).device if any(True for _ in model.parameters()) else torch.device('cpu')
    # ensure tensor on right device and has batch dim
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
