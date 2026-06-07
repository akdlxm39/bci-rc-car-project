# Overview

This folder contains repository-level notes for the cleaned project structure.

## What was done in the first cleanup pass
- created a GitHub-friendly top-level structure
- copied final artifacts into stable `FINAL_...` paths
- separated the final personalized training subset for `Participant2`
- copied non-final runtime development attempts into `05_experiments/runtime_dev/`
- separated non-training files (`foot0.csv`, `total.csv`, visualization PNGs`) from the curated training-ready dataset

## Final execution path
- Python runtime entrypoint: `../04_runtime/python/FINAL_main.py`
- Arduino sketch: `../04_runtime/arduino/FINAL_right_angle_rc.ino`
- Model files: `../03_models/final/`

## Curated data path
- training-ready dataset: `../02_data/training_ready/Participant2_filtered_final/`
- intermediate outputs: `../02_data/intermediate_outputs/`
- legacy excluded class sample: `../99_archive/legacy_class_foot/foot0.csv`

## Notes for GitHub publishing
Recommended approach:
1. keep the anonymized structure
2. use the curated `02_data/` subset instead of uploading every original dataset
3. decide separately whether large models/videos should stay in git or move to releases/LFS
4. keep original messy source folders only if they are still useful for provenance

## Next suggested cleanup steps
- add a reproducibility guide
- decide whether original source folders should stay or be ignored in git
- optionally deduplicate model files across `codes/learning`, `codes/realtime_test`, and `codes/mnt/data`
