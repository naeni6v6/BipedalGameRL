# BipedalGameRL 🦾

> ⚠️ **Work in Progress** — This project is currently under active development.

---

## Project Overview

A reinforcement learning project where an AI agent learns to walk and overcome obstacles in the BipedalWalker environment, themed around a college student commuting to a 9AM class at Korea University Sejong Campus.

---

## Concept

> "A university student robot trying to make it to 1st period class"

The agent starts by learning basic locomotion, then progressively tackles harder terrain — mirroring the struggle of waking up early for morning classes.

---

## Environment

| Item | Detail |
|------|--------|
| Base Environment | BipedalWalker-v3 (Gymnasium) |
| Challenge Environment | BipedalWalkerHardcore-v3 |
| Algorithm | PPO (Proximal Policy Optimization) |
| Library | Stable-Baselines3 |
| Hardware | NVIDIA RTX 3060 |

---

## Training Progress

| Stage | Steps | ep_rew_mean | Status |
|-------|-------|-------------|--------|
| Basic Walker | 1M | +216 | ✅ Complete |
| Hardcore | 3M | -62 | ✅ Complete |
| Hardcore | 5M | -35 | ✅ Complete |
| Hardcore | 10M | TBD | 🔄 Planned |

---

## Presentation Roadmap

| Presentation | Environment | Goal |
|-------------|-------------|------|
| 1st | Basic BipedalWalker | Verify basic locomotion |
| 2nd | Hardcore (first attempt) | Analyze failure on obstacles |
| Final | Hardcore (improved) + Custom Map | Complete campus-themed agent |

---

## Custom Map (Planned)

Korea University Sejong Campus theme:

| Element | Role |
|---------|------|
| Sinjeong Gate | Starting point |
| Campus road | Middle path |
| KU Flag | Landmark |
| Public Policy Hall | Final destination |

---

## File Structure
