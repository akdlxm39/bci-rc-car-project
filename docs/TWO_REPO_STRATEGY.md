# 두 저장소 분리 전략

이 문서는 프로젝트를 다음 두 저장소로 나누는 기준을 설명합니다.

1. `bci-rc-car-project`
2. `bci-rc-car-research`

핵심 아이디어는 단순합니다.
- `bci-rc-car-project`는 최종 결과물을 깔끔하게 보여주는 공개용 저장소입니다.
- `bci-rc-car-research`는 개발 과정과 실험 히스토리를 보존하는 연구용 저장소입니다.

---

## 1. 저장소별 역할

### `bci-rc-car-project`
**목적:** 최종 결과물을 보여주는 깔끔한 공개용 저장소

이 저장소에서는 다음을 보여줍니다.
- 최종 BCI RC카 시스템이 무엇인지
- 최종 파이프라인이 어떻게 동작하는지
- 실행 또는 설명에 필요한 핵심 파일이 무엇인지
- 최종 발표 자료, 모델, 런타임 코드가 무엇인지

이 저장소는 다음 성격을 유지하는 것이 좋습니다.
- 작고
- 읽기 쉽고
- 시연하기 쉽고
- 포트폴리오나 면접에서 빠르게 이해될 것

### `bci-rc-car-research`
**목적:** 개발 과정과 연구 히스토리를 보존하는 저장소

이 저장소에서는 다음을 보존합니다.
- 학기별 발표 자료 변화
- OpenViBE 단계 자료
- 전처리 및 특징 추출 실험
- 노트북 반복 실험 기록
- 최종 발표에 사용되지 않은 런타임 시도본
- 아카이브 자료와 출처 보존용 원본 구조

이 저장소는 다음 성격이어도 괜찮습니다.
- 용량이 크고
- 탐색적이며
- 아카이브 중심이고
- 초기에 비공개여도 무방함

---

## 2. 권장 공개 범위

### `bci-rc-car-project`
권장: **공개**

이유:
- 포트폴리오로 보여주기 좋음
- 공유가 쉬움
- 복잡한 실험 히스토리보다 최종 결과에 집중할 수 있음

### `bci-rc-car-research`
권장: **우선 비공개**, 이후 필요 시 일부만 공개

이유:
- 원본 과정 자료, 중복 데이터, 레거시 코드가 들어갈 수 있음
- 시간을 들여 안전하게 정리하기 좋음
- 쇼케이스 저장소보다 실험/출처 보존에 더 적합함

---

## 3. 각 저장소에 무엇을 둘지

## A. `bci-rc-car-project`

### 포함 권장
- `README.md`
- `docs/README.md`
- `docs/GITHUB_PUBLISHING_NOTES.md`
- `docs/TWO_REPO_STRATEGY.md`
- `presentation/FINAL_presentation_pretty.pptx`
- `models/FINAL_raw_data_model.pth`
- `models/FINAL_normalization_params.pth`
- `runtime/python/FINAL_main.py`
- `runtime/python/model.py`
- `runtime/python/signal_utils.py`
- `runtime/python/lsl_stream.py`
- `runtime/python/arduino_io.py`
- `runtime/arduino/FINAL_right_angle_rc.ino`
- `notebooks/FINAL_training_notebook.ipynb`
- `data/Participant2_filtered_final/`  
  (이 부분집합을 의도적으로 공개할 경우에만 포함)

### 기본 제외 권장
- 원본 EEG 폴더
- 예전 발표 버전 전체
- 실험 전용 노트북
- 최종 결과 설명에 꼭 필요하지 않은 OpenViBE 레거시 자료
- 최종본이 아닌 런타임 시도본
- 실험 과정에서 다른 위치에 중복 저장된 모델 파일

### 목표 구조
```text
bci-rc-car-project/
  README.md
  data/
  docs/
  models/
  notebooks/
  presentation/
  runtime/
    arduino/
    python/
```

---

## B. `bci-rc-car-research`

### 포함 권장
- 이전 발표 버전과 관련 보조 자료
- 보다 넓은 실험 노트북 모음
- OpenViBE 단계 산출물
- 전처리/특징 추출 실험 자료
- 최종 데모에 쓰이지 않은 런타임 개발 시도본
- 아카이브 자료
- 출처 보존이 필요한 원본 폴더 구조

### 권장 구조 예시
```text
bci-rc-car-research/
  README.md
  presentations/
  experiments/
  models/
  data/
  archive/
  docs/
```

---

## 4. 현재 공개 저장소 기준 매핑

| 현재 경로 | `bci-rc-car-project` | `bci-rc-car-research` | 비고 |
|---|---|---|---|
| `README.md` | 예 | 가능 | 공개 저장소용 README는 별도로 다듬어 유지 |
| `docs/` | 예 | 가능 | 전략 문서는 복사하거나 상황에 맞게 축약 가능 |
| `presentation/FINAL_presentation_pretty.pptx` | 예 | 예 | 최종 발표 자료는 두 저장소 모두에 유용함 |
| `models/FINAL_raw_data_model.pth` | 예 | 예 | 공개 저장소의 최종 산출물, 연구 저장소의 기준 산출물 |
| `models/FINAL_normalization_params.pth` | 예 | 예 | 위와 같은 이유로 두 저장소에 둘 수 있음 |
| `runtime/` | 예 | 예 | 최종 실행 경로의 핵심 |
| `notebooks/FINAL_training_notebook.ipynb` | 예 | 예 | 공개 저장소에는 요약된 최종 노트북, 연구 저장소에는 맥락 포함 자료로 유용 |
| `data/Participant2_filtered_final/` | 가능 | 예 | 공개 범위 승인이 있을 때만 공개 저장소에 유지 |

---

## 5. 강한 추천안

### `bci-rc-car-project`에는
최대한 핵심만 남깁니다.

추천 구성:
- 최종 README
- 최종 런타임 코드
- 최종 Arduino 코드
- 최종 모델 파일
- 최종 발표 자료
- 최종 학습 노트북 1개
- 필요 시 익명화된 예시 데이터 또는 학습용 부분집합만 포함

### `bci-rc-car-research`에는
과정을 남깁니다.

추천 구성:
- OpenViBE → PyTorch 전환 과정
- 전처리/특징 추출 실험 기록
- 노트북 반복 실험 이력
- 런타임 안정화 시도 기록
- 아카이브 및 출처 보존 자료

---

## 6. 실제 공개 순서 제안

### 1단계
먼저 `bci-rc-car-project`를 계속 다듬습니다.

이유:
- 바로 포트폴리오 가치가 생김
- 공개 검증이 상대적으로 쉬움

### 2단계
그 다음 `bci-rc-car-research`를 만듭니다.

이유:
- 더 천천히 정리해도 됨
- 대용량/히스토리 자료를 따로 관리하기 좋음

---

## 7. 최종 요약

### `bci-rc-car-project`
공개용, 깔끔함, 최종 결과물 중심

### `bci-rc-car-research`
우선 비공개, 히스토리와 실험 중심

이렇게 나누면 다음 장점이 있습니다.
- 하나는 결과를 보여주는 저장소가 되고
- 하나는 과정을 보존하는 저장소가 됩니다.
