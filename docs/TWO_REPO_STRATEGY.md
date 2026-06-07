# Two-Repository Strategy

This document defines how to split this project into two GitHub repositories:

1. `bci-rc-car-project`
2. `bci-rc-car-research`

---

## 1. Repository roles

### `bci-rc-car-project`
**Purpose:** public-facing final deliverable repository

Use this repo to show:
- what the final system is
- how it works
- what files are needed to run or explain it
- what the final artifacts are

This repo should be:
- small
- clear
- easy to read
- easy to present in a portfolio or interview

### `bci-rc-car-research`
**Purpose:** full development/research history repository

Use this repo to preserve:
- the semester-by-semester process
- experimental notebooks
- OpenViBE history
- preprocessing experiments
- model iteration history
- development attempts not used in the final presentation

This repo can be:
- larger
- more exploratory
- more archive-oriented

---

## 2. Recommended visibility

### `bci-rc-car-project`
Recommended: **public**

Reason:
- portfolio-friendly
- easy to share
- avoids overwhelming viewers with legacy material

### `bci-rc-car-research`
Recommended: **private** or **selectively public**

Reason:
- contains more raw process material
- may include redundant datasets, large files, legacy code, and experiment clutter
- easier to curate later if kept private first

---

## 3. What goes into each repo

## A. `bci-rc-car-project`

### Include
- `README.md`
- `00_overview/README.md`
- `00_overview/GITHUB_PUBLISHING_NOTES.md` (optional, or simplify)
- `01_presentations/4_final/FINAL_presentation_pretty.pptx`
- `03_models/final/FINAL_raw_data_model.pth`
- `03_models/final/FINAL_normalization_params.pth`
- `04_runtime/python/FINAL_main.py`
- `04_runtime/python/model.py`
- `04_runtime/python/signal_utils.py`
- `04_runtime/python/lsl_stream.py`
- `04_runtime/python/arduino_io.py`
- `04_runtime/arduino/FINAL_right_angle_rc.ino`
- `05_experiments/notebooks/learning/FINAL_training_notebook.ipynb`
- `02_data/training_ready/Participant2_filtered_final/` **only if dataset publication is acceptable**
- `02_data/intermediate_outputs/` **only selected explanatory files if needed**

### Exclude by default
- original participant root folders
- raw EEG data
- all old presentation trees
- all old notebooks
- OpenViBE legacy materials
- large videos unless intentionally published
- duplicated model files across experiment folders

### Goal structure
```text
bci-rc-car-project/
  README.md
  docs/
  presentation/
  models/
  runtime/
    python/
    arduino/
  notebooks/
  data/   # optional curated subset only
```

---

## B. `bci-rc-car-research`

### Include
- `01_presentations/1_midterm/`
- `01_presentations/2_final-term/`
- `01_presentations/3_second-semester-mid/`
- `01_presentations/4_final/`
- `05_experiments/`
- `99_archive/`
- `03_models/openvibe/`
- `03_models/experiments/` (if later organized)
- original `codes/data_creation/`
- original `codes/learning/`
- original `codes/realtime_test/`
- original participant/source folders if you want full provenance
- cleanup and organization docs

### Optional include
- curated top-level copies from the current cleaned structure
- selected datasets
- selected media

### Goal structure
```text
bci-rc-car-research/
  README.md
  presentations/
  experiments/
  archive/
  models/
  data/
  docs/
```

---

## 4. Mapping from current `~/졸프`

| Current path in `~/졸프` | `bci-rc-car-project` | `bci-rc-car-research` | Notes |
|---|---|---|---|
| `README.md` | Yes | Maybe | project repo should have its own rewritten README |
| `00_overview/` | Yes | Yes | can be split into public/private versions |
| `01_presentations/4_final/` | Yes | Yes | final repo keeps only final presentation |
| `01_presentations/1_midterm/` | No | Yes | research/history only |
| `01_presentations/2_final-term/` | No | Yes | research/history only |
| `01_presentations/3_second-semester-mid/` | No | Yes | research/history only |
| `02_data/training_ready/Participant2_filtered_final/` | Maybe | Yes | include publicly only if data sharing is acceptable |
| `02_data/intermediate_outputs/` | Selective | Yes | keep only explanatory files in project repo |
| `03_models/final/` | Yes | Yes | final repo definitely keeps this |
| `03_models/openvibe/` | No | Yes | research/history only |
| `04_runtime/` | Yes | Yes | final repo uses this as core deliverable |
| `05_experiments/notebooks/learning/FINAL_training_notebook.ipynb` | Yes | Yes | optional in project repo, definitely useful in research repo |
| `05_experiments/notebooks/learning/` full tree | No | Yes | research repo |
| `05_experiments/notebooks/realtime_test/` | No | Yes | research repo |
| `05_experiments/notebooks/data_creation/` | No | Yes | research repo |
| `05_experiments/runtime_dev/` | No | Yes | development attempt not used in final |
| `99_archive/` | No | Yes | archive only |
| original root participant folders | No | Optional | only if you want full provenance and data exposure is acceptable |
| original `codes/*` trees | No | Yes | research repo material |

---

## 5. Strong recommendation

### For `bci-rc-car-project`
Keep it minimal.

Best contents:
- final README
- final architecture/system explanation
- final runtime code
- final Arduino code
- final model
- final presentation
- maybe one final training notebook
- maybe curated anonymized sample data only

### For `bci-rc-car-research`
Keep the story.

Best contents:
- all presentation stages
- preprocessing attempts
- training notebook history
- realtime test history
- OpenViBE-to-PyTorch transition
- development notes and archives

---

## 6. Practical publishing plan

### Step 1
Create `bci-rc-car-project` first.

Why:
- easier to make clean quickly
- best immediate portfolio value

### Step 2
Create `bci-rc-car-research` second.

Why:
- can be curated more slowly
- may remain private initially

---

## 7. My recommendation for your case

### `bci-rc-car-project`
Public, clean, portfolio-focused

### `bci-rc-car-research`
Private first, then decide whether to open partially later

This gives you:
- one repo for showing the result
- one repo for preserving the journey

---

## 8. Next action

If approved, the next design step should be:
1. define exact directory trees for both repos
2. define which current files copy into each repo
3. then create the two repo-ready folders locally before git init
