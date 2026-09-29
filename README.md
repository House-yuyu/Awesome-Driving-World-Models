# Awesome Autonomous Driving World Models

A curated list of research papers on world models for autonomous driving, covering generative models, latent predictive models, world-action models, and JEPA-based representation learning.

This repository focuses on world-model-related research rather than the full autonomous-driving stack. Related work from robotics and video generation is included as reference.

> **11 papers** · Last updated: 2026-09-29 · PRs welcome

## Scope

- Generative driving world models
- Latent and predictive world models
- World-action models
- JEPA-based driving representation learning
- Related embodied and video world models

## Recent Updates

- **2026-09-29** — Initialized the curated paper list with structured metadata and categorized recent work on driving world models.

<!-- PAPERS_START -->

## Contents

- [Surveys & Perspectives](#surveys-perspectives)
- [Driving World Models](#driving-world-models)
  - [Generative World Models](#generative-world-models)
  - [Latent / Predictive World Models](#latent--predictive-world-models)
  - [World-Action Models](#world-action-models)
- [Representation Learning](#representation-learning)
  - [JEPA-based Methods](#jepa-based-methods)
- [Related Work](#related-work)
  - [Embodied / Robotics World Models](#embodied--robotics-world-models)
  - [General Video World Models](#general-video-world-models)

## Surveys & Perspectives

| Model | Title | Focus | Venue | Resources |
| --- | --- | --- | --- | --- |
| **Embodied WM Survey** | [World Models for Embodied Intelligence: From Plausible to Controllable to Actionable](https://arxiv.org/abs/2609.16697) | Embodied world model survey | arXiv '26 | — |

## Driving World Models

### Generative World Models

| Model | Title | Focus | Venue | Resources |
| --- | --- | --- | --- | --- |
| **HelloWorld** | [HelloWorld: Towards Practical Applications of Generative Driving World Models](https://arxiv.org/abs/2609.28931) | Generative driving simulation | arXiv '26 | [Project](https://helloworld-4d.github.io) |

### Latent / Predictive World Models

| Model | Title | Focus | Venue | Resources |
| --- | --- | --- | --- | --- |
| **Auto-JEPA** | Auto-JEPA: A Latent World Model of Continuous Intent for End-to-End Autonomous Driving | Latent intent prediction | arXiv '26 | [Code](https://github.com/NoctYang/Auto-JEPA) |
| **Drive-JEPA** | [Drive-JEPA: Video JEPA Meets Multimodal Trajectory Distillation for End-to-End Driving](https://arxiv.org/abs/2601.22032) | Video JEPA + trajectory distillation | arXiv '26 | [Code](https://github.com/linhanwang/Drive-JEPA) |
| **ForeDrive** | ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model | Planning-relevant latent prediction | arXiv '26 | — |
| **WALT** | [WALT: Learning World-Model-Aligned Latent Trajectories for Autonomous Driving](https://arxiv.org/abs/2609.30436) | WM-aligned trajectory learning | arXiv '26 | — |

### World-Action Models

| Model | Title | Focus | Venue | Resources |
| --- | --- | --- | --- | --- |
| **MM-Future** | MM-Future: Multi-Mode Joint World-Action Modeling for Autonomous Driving | Multi-mode world-action modeling | arXiv '26 | — |
| **WA-JEPA** | WA-JEPA: Rethinking the Video JEPA Paradigm for World-Action Modeling in Autonomous Driving | JEPA-based world-action modeling | arXiv '26 | [Code](https://github.com/AFARI-Research/WA-JEPA) |

## Representation Learning

### JEPA-based Methods

| Model | Title | Focus | Venue | Resources |
| --- | --- | --- | --- | --- |
| **AD-L-JEPA** | [Self-Supervised Representation Learning with Joint Embedding Predictive Architecture for Automotive LiDAR Object Detection (AD-L-JEPA)](https://arxiv.org/abs/2501.4969) | LiDAR representation pre-training | arXiv '25 | — |

## Related Work

### Embodied / Robotics World Models

| Model | Title | Focus | Venue | Resources |
| --- | --- | --- | --- | --- |
| **XPACE** | [XPACE: Joint World and Action Modeling from Heterogeneous Experience](https://arxiv.org/abs/2609.17372) | Robotic world-action modeling | arXiv '26 | [Project](https://xpeng-robotics.github.io/xpace/) |

### General Video World Models

| Model | Title | Focus | Venue | Resources |
| --- | --- | --- | --- | --- |
| **HOLO-WORLD** | [HOLO-WORLD: Unified Camera, Object and Weather Control for Video World Model](https://arxiv.org/abs/2606.20083) | Controllable video world model | arXiv '26 | [Project](https://xiangchenyin.github.io/Holo-World/) |

<!-- PAPERS_END -->

## Terminology

| Abbreviation | Meaning |
|---|---|
| WM | World Model |
| WAM | World-Action Model |
| JEPA | Joint-Embedding Predictive Architecture |
| E2E | End-to-End |

## Repository Structure

Paper metadata lives in `data/papers.yaml` and the README tables are auto-generated.

```text
.
├── README.md
├── data/
│   └── papers.yaml
├── scripts/
│   └── generate_readme.py
└── requirements.txt
```

## Contributing

Contributions are welcome. To add or update a paper:

1. Edit the entry in `data/papers.yaml`
2. Regenerate the README:
   ```bash
   pip install -r requirements.txt
   python scripts/generate_readme.py
   ```
3. Open a pull request

The script only updates content between the `<!-- PAPERS_START -->` and `<!-- PAPERS_END -->` markers; everything else is edited manually.
