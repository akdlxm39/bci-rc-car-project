# BCI RC카 프로젝트

> **Muse 2, PyTorch, LSL, BLE(HM-10), Arduino**를 활용해  
> **뇌파(EEG) 기반으로 RC카를 실시간 제어**한 프로젝트입니다.

## 프로젝트 개요
이 프로젝트는 뇌파를 입력 인터페이스로 활용해, 사용자의 의도를 실시간으로 분류하고  
그 결과를 RC카 제어 명령으로 연결하는 **BCI(Brain-Computer Interface)** 시스템을 구현하는 것을 목표로 합니다.

최종 시스템은 다음 흐름으로 동작합니다.

1. **Muse 2** 헤드셋으로 EEG 신호를 측정
2. 주파수 대역별 특징(feature) 추출
3. **PyTorch 분류 모델**로 사용자 의도 분류
4. 분류 결과를 **BLE(HM-10)** 로 Arduino에 전송
5. Arduino가 RC카를 실제로 제어

이 저장소는 프로젝트의 **최종 결과물 중심 공개용 저장소**입니다.  
최종 발표 자료, 최종 실행 코드, 최종 모델을 포함합니다.

---

## 시스템 동작 정의

### 분류 클래스
- `left`
- `right`
- `blink`
- `none`

### RC카 제어 매핑
- `left` → 좌회전
- `right` → 우회전
- `blink` → 직진
- `none` → 직진

### 최종 제어 방식
최종 구현에서는 `blink`와 `none`을 모두 **전진 계열 상태**로 사용하고,  
`left`, `right`는 **직각 회전** 동작으로 연결했습니다.

---

## 기술 구성

### 하드웨어
- **Muse 2** EEG 헤드셋
- **HM-10 BLE 모듈**
- **Arduino 기반 RC카**

### 소프트웨어
- **PyTorch**: 뇌파 분류 모델
- **LSL (Lab Streaming Layer)**: 실시간 EEG 스트리밍
- **Python**: 실시간 추론 및 BLE 통신
- **Arduino**: RC카 모터 제어

---

## 특징 추출 방식
최종 파이프라인에서는 **4개 채널**과 **5개 주파수 대역**을 사용해  
총 **20차원 feature vector**를 구성합니다.

### 사용 채널
- TP9
- AF7
- AF8
- TP10

### 사용 주파수 대역
- Alpha: 8–12 Hz
- Beta 1: 12–20 Hz
- Beta 2: 20–30 Hz
- Gamma 1: 30–35 Hz
- Gamma 2: 35–40 Hz

즉,

- **4채널 × 5대역 = 20차원 feature**

로 구성됩니다.

---

## 저장소 구성

```text
bci-rc-car-project/
  data/
  docs/
  models/
  notebooks/
  presentation/
  runtime/
```

- `data/`  
  공개 가능한 EEG 데이터 subset 및 중간 산출물
- `docs/`  
  저장소 설명 및 배포 관련 문서
- `models/`  
  최종 학습 모델 파일
- `notebooks/`  
  최종 학습 노트북
- `presentation/`  
  최종 발표 자료
- `runtime/`  
  최종 실행 Python / Arduino 코드

---

## 주요 파일

### 최종 발표 자료
- `presentation/FINAL_presentation_pretty.pptx`

### 최종 실행 코드
- `runtime/python/FINAL_main.py`

### 최종 Arduino 코드
- `runtime/arduino/FINAL_right_angle_rc.ino`

### 최종 모델
- `models/FINAL_raw_data_model.pth`
- `models/FINAL_normalization_params.pth`

### 최종 학습 노트북
- `notebooks/FINAL_training_notebook.ipynb`

---

## 프로젝트 의의
이 프로젝트는 뇌파 기반 BCI가 단순한 소프트웨어 분류 실험을 넘어서,  
**실제 물리 시스템(RC카)** 과 연결될 수 있음을 보여주는 예시입니다.

또한 다음과 같은 현실적인 문제들을 함께 다룹니다.

- EEG 신호의 개인차
- 전처리 방식의 영향
- 실시간 제어와 분류 정확도의 차이
- 실제 사용 가능한 동작 설계의 어려움
