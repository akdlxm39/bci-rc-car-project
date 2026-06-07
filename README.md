# BCI RC Car Project

> **EEG-based brain-computer interface project for controlling an RC car in real time** using **Muse 2**, **PyTorch**, **LSL**, **BLE (HM-10)**, and **Arduino**.

## Overview
This project explores how brainwave signals can be used as an input interface for physical control.
We built a pipeline that:

1. measures EEG signals from a **Muse 2** headset,
2. preprocesses the signal into band-based features,
3. classifies user intent with a **PyTorch** model,
4. sends the predicted command to an **Arduino-controlled RC car**,
5. executes real-world motion such as left turn, right turn, and forward movement.

This repository is the **clean public-facing deliverable** version of the project.
It contains the final runtime code, final model artifacts, final presentation, and a curated public EEG dataset subset.

---

## What the system does
### Signal classes
- `left`
- `right`
- `blink`
- `none`

### Control mapping
- `left` → left turn
- `right` → right turn
- `blink` → forward
- `none` → forward

### Core idea
The system maps EEG-derived intent classes to RC car commands in real time.
In the final setup, `blink` and `none` were both treated as forward-driving states, while `left` and `right` triggered right-angle turning behavior.

---

## Technical pipeline
### Hardware
- **Muse 2** EEG headset
- **HM-10 BLE module**
- **Arduino-based RC car**

### Software
- **PyTorch** for intent classification
- **LSL (Lab Streaming Layer)** for real-time EEG streaming
- **Python** for runtime inference and communication
- **Arduino** for motor control

### Feature extraction
The project uses **4 EEG channels** and **5 frequency bands**, producing a **20-dimensional feature vector**:
- Alpha: 8–12 Hz
- Beta 1: 12–20 Hz
- Beta 2: 20–30 Hz
- Gamma 1: 30–35 Hz
- Gamma 2: 35–40 Hz

---

## Repository contents
### Final artifacts
- Final presentation: `presentation/FINAL_presentation_pretty.pptx`
- Final runtime entrypoint: `runtime/python/FINAL_main.py`
- Final Arduino sketch: `runtime/arduino/FINAL_right_angle_rc.ino`
- Final model weights: `models/FINAL_model2_3_jh_just_new.pth`
- Final normalization params: `models/FINAL_norm_params2_3_jh_just_new.pth`
- Final training notebook: `notebooks/FINAL_training_notebook.ipynb`

### Public data included here
- Curated training-ready EEG subset: `data/Participant2_filtered_final/`
- Intermediate analysis outputs: `data/intermediate_outputs/`
- Legacy excluded class sample: `data/legacy_class_foot/foot0.csv`

---

## Project structure
```text
bci-rc-car-project/
  data/
  docs/
  models/
  notebooks/
  presentation/
  runtime/
```

- `data/` — curated public EEG subset and derived outputs
- `docs/` — publishing and repository notes
- `models/` — final trained model artifacts
- `notebooks/` — final training notebook
- `presentation/` — final presentation deck
- `runtime/` — final Python + Arduino execution code

---

## Participant anonymization
Public-facing data and documentation use anonymized participant labels:
- `Participant1`
- `Participant2`
- `Participant3`

The curated final personalized training subset included in this repository is based on **Participant2**.

---

## Related repository
The full development history, experiments, and legacy materials are separated into a companion research repository:
- `bci-rc-car-research`

This split keeps the present repository focused on the final result while preserving the broader R&D process elsewhere.

---

## Why this project matters
This project is a small but concrete example of how **brain-computer interfaces** can move beyond software-only demos and connect directly to **physical systems**.
It also highlights practical challenges in BCI work, including:
- signal variability,
- preprocessing choices,
- per-user differences,
- real-time control constraints,
- and the gap between classification accuracy and usable physical interaction.

---

## Notes
- This repository prioritizes clarity and final deliverables over full experimental history.
- Large-scale research artifacts and earlier workflow iterations are intentionally kept outside this repo.
- EEG files included here are intentionally public and anonymized for this project context.
