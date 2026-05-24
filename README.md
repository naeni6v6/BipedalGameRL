# BipedalGameRL 🦾

> ⚠️ **Work in Progress** — This project is currently under active development.

## Project Overview

End-to-end deep reinforcement learning project implementing **Proximal Policy Optimization (PPO)** to solve continuous control locomotion tasks in the OpenAI Gymnasium `BipedalWalkerHardcore-v3` environment.

This project demonstrates practical experience in **policy gradient methods, reward engineering, hyperparameter tuning, and training pipeline construction** — core competencies for ML engineering roles.

## Key Skills Demonstrated

| Category | Detail |
|----------|--------|
| Reinforcement Learning | PPO, policy gradient, reward shaping |
| Deep Learning | Actor-Critic architecture, MLP policy |
| MLOps | Checkpoint management, model versioning, training pipeline |
| Experiment Design | Curriculum learning, hyperparameter tuning |
| Visualization | Training curve analysis, video recording |
| Tools | PyTorch, Stable-Baselines3, Gymnasium, CUDA |

## Environment

| Item | Detail |
|------|--------|
| Base Environment | BipedalWalker-v3 (Gymnasium) |
| Challenge Environment | BipedalWalkerHardcore-v3 |
| Observation Space | 24-dimensional continuous state vector |
| Action Space | 4-dimensional continuous joint torque control |
| Hardware | NVIDIA RTX 3060 (CUDA acceleration) |

## Approach

Rather than directly training on the hardcore environment, this project adopts a **curriculum learning strategy** — first establishing a stable baseline policy on the standard environment, then transferring and fine-tuning on the obstacle-rich hardcore variant. This approach reflects real-world ML practices where progressive task complexity leads to more robust model generalization.

## Hyperparameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| learning_rate | 0.0001 | Conservative update for stable hardcore training |
| n_steps | 4096 | Larger rollout buffer for complex environment |
| batch_size | 256 | Balanced memory efficiency and gradient stability |
| gamma | 0.99 | Long-horizon reward consideration |
| device | CUDA | GPU-accelerated training via RTX 3060 |

## Training Progress

| Stage | Steps | ep_rew_mean | Status |
|-------|-------|-------------|--------|
| Baseline (BipedalWalker) | 1M | +216 | ✅ Complete |
| Hardcore Phase 1 | 3M | -62 | ✅ Complete |
| Hardcore Phase 2 | 5M | -35 | ✅ Complete |
| Hardcore Phase 3 | 10M | TBD | 🔄 In Progress |

> ep_rew_mean improved from -62 → -35 between 3M and 5M steps, confirming stable policy convergence.

## Repository Structure
