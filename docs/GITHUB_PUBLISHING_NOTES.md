# GitHub Publishing Notes

## Current recommendation
This repository has been reorganized to support a cleaner public-facing structure, but you should still review what to publish.

## Safe-to-review primary paths
- `README.md`
- `00_overview/`
- `01_presentations/4_final/`
- `03_models/final/`
- `04_runtime/`
- `05_experiments/notebooks/learning/FINAL_training_notebook.ipynb`

## Review carefully before public push
- any remaining original folders containing raw or participant-specific files
- large media under original presentation folders
- duplicated datasets across `codes/learning`, `codes/realtime_test`, and legacy trees
- model binary size and whether Git LFS is preferable

## Anonymization policy used here
- public docs use `Participant1`–`Participant5`
- final personalized training set is documented as `Participant2`
- non-used participant folders are treated as archive candidates

## Recommended future cleanup
- add a small sample dataset only, if full data should not be public
- add exact environment setup instructions for Python/LSL/BLE dependencies
- decide whether presentation source media should stay in-repo or move out to release assets
