# GAN-Based Data Augmentation for PCB Defect Detection

Generative data augmentation for printed circuit board (PCB) defect detection, built to address ISRO-SAC's **"PCB Long-Tail Effect"** problem statement. Starting from only **690 real samples**, this project benchmarks three GAN architectures and a weighted ensemble to synthesize realistic defect images, then validates their usefulness on a downstream classifier.

> Published in the *Proceedings of the 11th International Congress on Information and Communication Technology (ICICT 2026)*, London, UK.
> Recipient of the **Best Research Project Award**, PESU Research Foundation.

---

## Problem

PCB defect detection suffers from the long-tail effect: some defect classes are rare, so classifiers see very few examples of them. With only 690 real samples available, a classifier trained on real data alone performs poorly. This project asks whether synthetic images from GANs can close that gap.

## Approach

1. **Generate:** Implemented and benchmarked 3 GAN architectures plus a weighted ensemble to synthesize PCB defect images.
2. **Measure image quality:** Compared models using Fréchet Inception Distance (FID).
3. **Measure usefulness:** Evaluated synthetic data with a **Train-on-Synthetic, Test-on-Real (TSTR)** protocol, checking whether a classifier trained with the synthetic data improves on real held-out samples.

## Results

| Metric | Result |
|---|---|
| Best model | **cWGAN-GP** |
| Best FID | **1.17** |
| Classifier F1 (real data only) | 0.081 |
| Classifier F1 (with cWGAN-GP augmentation) | **0.207** |
| Improvement | **155%** |

### Models benchmarked

- cWGAN-GP (best performing)
- [Architecture 2: add name]
- [Architecture 3: add name]
- Weighted ensemble of the above

## Tech stack

Python, PyTorch, [add: torchvision, OpenCV, scikit-learn, etc.]

## Repository structure

```
.
├── data/              # [describe dataset layout]
├── models/            # [GAN architectures]
├── train.py           # [training entry point]
├── evaluate.py        # [FID and TSTR evaluation]
├── notebooks/         # [experiments]
└── README.md
```

> Update this tree to match your actual repo.

## Getting started

```bash
git clone [repo-url]
cd [repo-name]
pip install -r requirements.txt
```

**Train:**
```bash
python train.py --model cwgan_gp --epochs [N]
```

**Evaluate (FID and TSTR):**
```bash
python evaluate.py --model cwgan_gp
```

> Replace the commands and flags above with your actual ones.

## Dataset

[Describe the dataset: source, 690 real samples, defect classes, image size, train/test split. Note any licensing or confidentiality limits, since the problem statement came from ISRO-SAC.]

## Citation

```bibtex
@inproceedings{joshi2026pcbgan,
  title     = {Data Augmentation for Printed Circuit Board Defect Detection: A Performance-Based Analysis of GAN Architectures},
  author    = {Joshi, Aniruddha and [co-authors]},
  booktitle = {Proceedings of the 11th International Congress on Information and Communication Technology (ICICT 2026)},
  address   = {London, UK},
  year      = {2026}
}
```

## Acknowledgments

Conducted during a summer internship at PESU Research Foundation (July to September 2025), based on the ISRO-SAC "PCB Long-Tail Effect" problem statement.

## Author

**Aniruddha Joshi**
B.Tech CSE (AI & ML), PES University, Bengaluru
[GitHub] | [LinkedIn]
