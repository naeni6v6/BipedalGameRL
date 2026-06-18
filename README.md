# 🦾 Training a Bipedal Agent with PPO on Hardcore Terrain

## Overview
A deep reinforcement learning project training a bipedal agent to navigate randomized hardcore terrain using **PPO (Proximal Policy Optimization)**.  
Goes beyond running a script — includes failure analysis, evaluation methodology, and targeted fine-tuning across 8 training phases.

## Training Phases

| Phase | Steps | Eval Score (50-ep avg) | Note |
|-------|-------|------------------------|------|
| Baseline (Standard) | 1M | +216 | Warm-up on standard env |
| Hardcore Curriculum | 5M | — | Curriculum learning |
| Large-scale | 20M | +62.24 | LR floor fix applied |
| **Stump Fine-tune (Final)** | **+2M** | **+64.32** | Targeted weakness patch |

> Honest baseline (50-ep): **-17.53** → Final: **+64.32** (+81.85 pts)

## Key Engineering Insights

**CPU > GPU for this task**  
`MlpPolicy` + `Box2D` is CPU-bound. `SubprocVecEnv` with `n_envs=8` achieved ~1,442 fps vs ~521 fps on CUDA.

**Evaluation reliability**  
10-episode peak (+46.23) collapsed to -17.53 on 50-episode re-validation. All phase comparisons standardized to 50-episode averages.

**LR exhaustion as failure mode**  
Reward collapse at 6–7M steps traced to LR decaying to near-zero. Fixed with an LR floor (`2e-5`); `explained_variance` reached 0.892 by end of training.

## Weakness Analysis & Fix

Video inspection revealed consistent failure at **stump obstacles**. Quantified the gap:

| Env | Score (50-ep) |
|-----|--------------|
| Standard Hardcore | +57.09 |
| Stump-heavy | +24.66 (**-32.43**) |

Phase 8 fine-tuned from the pre-degradation checkpoint with elevated stump frequency → **+15.01 on stumps, -2.57 on standard** (within noise).

## Results

| Metric | Value |
|--------|-------|
| Final eval score (50-ep) | **+64.32** |
| Best single-episode score | **292.3** / 300 |
| Total improvement from baseline | **+81.85 pts** |

## Tech Stack
Python, PyTorch, Stable-Baselines3, Gymnasium  
PPO, Curriculum Learning, SubprocVecEnv, Grad-CAM, VecNormalize

## Limitations & Future Work
High episode-level variance is inherent to randomized hardcore terrain (std ~105).  
Future work: further stump fine-tuning, ensemble checkpoints, SAC/TD3 comparison.
