# 🌌 Transit Explorer

**Transit Explorer** is an open-source Python tool for downloading, processing, and visualizing astronomical light curves from NASA's **TESS** and **Kepler** missions.

The program automatically downloads public photometric observations, detects periodic transit signals using the **Box Least Squares (BLS)** algorithm, folds the light curve, and produces publication-quality visualizations.

This project was created as an educational and research tool for students, astronomy enthusiasts, and anyone interested in exoplanet transit analysis.

---

## Features

- Download light curves directly from NASA archives
- Support for both **TESS** and **Kepler**
- Automatic light curve normalization
- Automatic orbital period detection using BLS
- Phase-folded transit visualization
- BLS periodogram visualization
- Automatic figure export
- Easy configuration through a single settings section

---

## Workflow


Download observations
        ↓
Normalize light curve
        ↓
Search orbital period (BLS)
        ↓
Fold light curve
        ↓
Generate scientific plots
        ↓
Save results


---

## Repository Structure

```
Transit-Explorer/
│
├── transit_explorer.py
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── examples/
│
└── results/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/arsantsoy-sudo/Transit-Explorer.git
cd Transit-Explorer
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

- Python 3.10+
- Lightkurve
- Astropy
- Astroquery 
- NumPy 
- Matplotlib

---

## Configuration

All settings are located at the beginning of the script.

Example:

```python
TARGET = "KELT-9b"

MISSION = "TESS"

SECTOR = 14

QUARTER = None

PERIOD_MIN = 1.2
PERIOD_MAX = 1.7
PERIOD_STEP = 0.0001

TRANSIT_DURATION = 0.15

BIN_SIZE = 0.002

PHASE_WINDOW = 0.20
```

Changing only these parameters allows the program to analyze different astronomical objects.

---

## Example Output

The program produces:

- Raw light curve
- Normalized light curve
- Box Least Squares periodogram
- Phase-folded transit profile

Example using **KELT-9b**

<img width="1800" height="1400" alt="KELT-9b_transit" src="https://github.com/user-attachments/assets/cec08fd4-29a9-49ba-a0f9-210baf4fe620" />

---

## Scientific Background

 When an exoplanet passes in front of its host star, it blocks a small fraction of the stellar light.
These periodic decreases in brightness are called **transits**.
Transit Explorer detects these periodic signals using the **Box Least Squares (BLS)** algorithm and reconstructs the transit profile by folding the light curve using the detected orbital period.

---

## Future Development

Planned features include:

- Automatic processing of multiple targets
- Transit parameter extraction
- CSV export

---

## License

This project is released under the MIT License.

---

## Author

**Arsan Tsoy**

Student researcher interested in:

- Exoplanets
- Astrobiology
- Data Science
- Machine Learning

GitHub: https://github.com/arsantsoy-sudo
