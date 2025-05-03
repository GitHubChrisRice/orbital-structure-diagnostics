# Orbital Structure Diagnostics via Canonical Summation and Entropy

This repository contains the source code and figure outputs for the manuscript:

**"Orbital Structure Analysis via Canonical Summation and Entropy Diagnostics: A Non-Spectral Framework for Classifying Quantum Probability Clouds"**

## Overview

This work introduces two structural diagnostics derived directly from radial electron density profiles:
- **Canonical Summation** \( \mathcal{S}_\psi(L; s) \): a scale-weighted accumulation of probability mass, sensitive to spatial extent and layering.
- **Radial Entropy** \( \mathcal{H}_\psi(N) \): a bin-based measure of distribution complexity, revealing shell structure and delocalization.

These tools provide a potential non-spectral alternative to orbital classification, applicable to both analytic wavefunctions and numerical densities (e.g., from DFT).

## Contents

/scripts/ # Python and SageMath scripts for loading cube files, computing diagnostics, and plotting
/figures/ # EPS versions of all figures used in the manuscript
/data/ # CSV files of computed radial densities and diagnostics (for reproducibility)
/cube_files/ # DFT-derived .cube files used in the NH3, H2O, and Li case studies
README.md # This file
LICENSE # Creative Commons Attribution 4.0 (CC BY 4.0)


## Computational Notes

- All DFT calculations were performed using `psi4` with the B3LYP/sto-3g method, for consistency and accessibility.
- We acknowledge that STO-3G is a minimal basis set not suitable for high-precision densities; it is used here solely to demonstrate the qualitative behavior of the diagnostics.
- Future versions of this framework will include support for cc-pVTZ and aug-cc-pVQZ basis sets, as well as benchmarking against established descriptors like ELF and QTAIM.

## How to Run

The pipeline is fully reproducible:

1. Install `psi4`, `numpy`, `matplotlib`, and `scipy`.
2. Run `psi4 <molecule>.py` to generate a density cube.
3. Use `cube_to_radial_density_<molecule>.py` to extract radial density.
4. Use `diagnostics_<molecule>.py` to generate summation and entropy plots.

Example:
```bash
sage -python cube_to_radial_density_nh3.py
sage -python diagnostics_nh3.py
