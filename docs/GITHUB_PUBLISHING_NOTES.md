# GitHub 공개 점검 메모

## 목적
이 문서는 `bci-rc-car-project` 저장소를 공개 상태로 유지할 때 어떤 파일을 우선 점검해야 하는지 정리한 간단한 체크리스트입니다.

## 공개 푸시 전 우선 점검 대상
- `README.md`
- `docs/`
- `presentation/FINAL_presentation_pretty.pptx`
- `models/FINAL_raw_data_model.pth`
- `models/FINAL_normalization_params.pth`
- `runtime/python/`
- `runtime/arduino/FINAL_right_angle_rc.ino`
- `notebooks/FINAL_training_notebook.ipynb`
- `data/Participant2_filtered_final/`  
  (이 부분집합을 의도적으로 공개할 때만 유지)

## 공개 상태로 남기기 전에 특히 주의할 항목
- 추가로 들어온 참여자별 데이터나 원본 EEG 파일
- 대용량 미디어 파일이나 중복 바이너리
- 최종 발표에 쓰이지 않은 실험용 노트북/런타임 시도본
- 예전 로컬 폴더 구조나 불필요한 출처 정보가 드러나는 파일

## 익명화 원칙
- 공개 문서에서는 `Participant1`, `Participant2` 같은 형식을 사용합니다.
- 현재 이 저장소의 최종 개인화 학습 데이터는 `Participant2`로 표기합니다.
- 실제 이름이나 원본 참여자 폴더명이 다시 공개 문서에 들어오지 않도록 주의합니다.

## 권장 공개 방향
- 이 저장소는 최종 시스템과 그 설명에 집중합니다.
- 더 넓은 실험 과정, OpenViBE 시기 자료, 아카이브성 히스토리는 별도 연구용 저장소로 분리합니다.
- 바이너리 파일이 더 커지면 GitHub Releases 또는 Git LFS 사용을 검토합니다.

## 푸시 전 빠른 확인 목록
푸시 전에 아래 항목을 빠르게 확인합니다.
1. README 설명이 현재 파일 구조와 일치하는가?
2. 문서 속 실행 경로가 `runtime/python/`, `runtime/arduino/`를 정확히 가리키는가?
3. 문서에 적힌 모델 이름이 `models/` 아래 실제 파일명과 일치하는가?
4. 새로 추가한 파일이 원본 데이터나 불필요한 참여자 정보를 노출하지 않는가?
