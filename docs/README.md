# 문서 안내

이 `docs/` 폴더에는 공개용 `bci-rc-car-project` 저장소를 설명하고 관리하기 위한 보조 문서가 들어 있습니다.

## 문서 구성
- `README.md` — 문서 폴더 전체 안내
- `GITHUB_PUBLISHING_NOTES.md` — 공개 저장소로 유지할 내용을 점검하는 체크리스트
- `TWO_REPO_STRATEGY.md` — 공개용 저장소와 연구/히스토리 저장소를 어떻게 분리할지에 대한 정리

## 현재 공개 저장소 구조
현재 저장소는 최종 결과물을 중심으로 다음과 같이 구성되어 있습니다.

```text
bci-rc-car-project/
  README.md
  data/
    Participant2_filtered_final/
  docs/
  models/
  notebooks/
  presentation/
  runtime/
    arduino/
    python/
```

## 최종 실행 산출물
- Python 실행 진입점: `../runtime/python/FINAL_main.py`
- Arduino 스케치: `../runtime/arduino/FINAL_right_angle_rc.ino`
- 모델 파일:
  - `../models/FINAL_raw_data_model.pth`
  - `../models/FINAL_normalization_params.pth`
- 최종 학습 노트북: `../notebooks/FINAL_training_notebook.ipynb`
- 최종 발표 자료: `../presentation/FINAL_presentation_pretty.pptx`

## 공개된 데이터 범위
- 개인화 학습용으로 정리한 부분집합: `../data/Participant2_filtered_final/`
- 공개 문서에서는 `Participant2`처럼 익명화된 참여자 표기를 사용합니다.
- 원본 EEG 폴더와 더 넓은 실험 히스토리는 이 공개 저장소에 포함하지 않는 것을 기본 원칙으로 합니다.

## 공개 저장소 운영 원칙
이 저장소는 다음 원칙으로 유지하는 것을 권장합니다.
1. 최종 결과물 중심 구조를 유지한다.
2. 참여자 표기는 익명화된 형식으로 유지한다.
3. 대용량 바이너리 파일은 계속 git에 둘지, Releases나 Git LFS로 옮길지 검토한다.
4. 실험 히스토리, 레거시 코드, 원본 자료는 필요 시 별도의 연구용 저장소로 분리한다.

## 앞으로 더 보완하면 좋은 항목
- Python, LSL, BLE, Arduino 의존성 설치 가이드 추가
- 최종 데모 파이프라인 재현 절차 문서 추가
- 현재 공개 데이터 부분집합을 유지할지, 더 작은 예시 데이터만 남길지 검토
