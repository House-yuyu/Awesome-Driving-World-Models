# Awesome Driving World Models 🚗🌎

<p align="center">
  <img src="https://img.shields.io/badge/papers-41-blue" alt="Papers">
  <img src="https://img.shields.io/badge/last%20updated-2026--09--30-brightgreen" alt="Last Updated">
  <img src="https://img.shields.io/badge/PRs-welcome-orange" alt="PRs Welcome">
</p>

A curated collection of research on **world models for autonomous driving**, spanning **generative simulation**, **explicit-state prediction**, **latent future modeling**, **world-action modeling**, and **JEPA-based representation learning**.

> **From predicting observations to learning decision-relevant futures and actions.**

This repository focuses on **world-model-related research rather than the full autonomous-driving stack**. Selected work from robotics, embodied intelligence, and general video world models is included when it introduces ideas directly relevant to driving-world prediction, controllability, or action-conditioned modeling.

---

## Scope

The collection is organized by **what the model predicts and how that prediction is used**, rather than by architecture name alone.

```text
Driving World Models
├── Generative & Explicit-State World Models
│   ├── RGB / multi-view video
│   ├── LiDAR / point clouds
│   ├── BEV / occupancy / 3D worlds
│   └── multimodal scene generation
│
├── Latent & Planning-Oriented World Models
│   ├── latent future prediction
│   ├── planning-relevant representations
│   ├── model-based imitation / reinforcement learning
│   └── future-conditioned planning
│
├── World-Action & Action-Aligned Models
│   ├── joint future-world / action prediction
│   └── world-model-aligned action representations
│
└── Driving Representation Learning
    └── JEPA-based predictive representation learning

Related Work
├── Embodied / Robotics World Models
└── General Video World Models
```

### What is included?

A paper is generally included when **future-world prediction, learned environment dynamics, latent future modeling, or world-action coupling is a central part of the method**.

General perception, planning, VLM/VLA, or video-generation papers are not included unless they have a clear world-model connection.

---

## Contents

- [Surveys & Perspectives](#surveys--perspectives)
- [Driving World Models](#driving-world-models)
  - [Generative & Explicit-State World Models](#generative--explicit-state-world-models)
  - [Latent & Planning-Oriented World Models](#latent--planning-oriented-world-models)
  - [World-Action & Action-Aligned Models](#world-action--action-aligned-models)
- [Driving Representation Learning](#driving-representation-learning)
  - [JEPA-based Methods](#jepa-based-methods)
- [Related Work](#related-work)
  - [Embodied / Robotics World Models](#embodied--robotics-world-models)
  - [General Video World Models](#general-video-world-models)
- [Recent Updates](#recent-updates)
- [Concepts](#concepts)
- [Contributing](#contributing)
- [Repository Structure](#repository-structure)
- [Inclusion Criteria](#inclusion-criteria)

---

<!-- PAPERS_START -->

# Surveys & Perspectives

| Work | Paper | Focus | Venue | Resources |
| --- | --- | --- | --- | --- |
| **Latent WM Survey** | [Latent World Models for Automated Driving: A Unified Taxonomy, Evaluation Framework, and Open Challenges](https://arxiv.org/abs/2603.09086) | Latent-state taxonomy, evaluation, and deployment challenges | arXiv 2026 | — |
| **DWM Survey** | [The Role of World Models in Shaping Autonomous Driving: A Comprehensive Survey](https://arxiv.org/abs/2502.10498) | Driving world models by predicted scene modality | arXiv 2025 | [Paper List](https://github.com/LMD0311/Awesome-World-Model) |
| **WMAD Survey** | [A Survey of World Models for Autonomous Driving](https://arxiv.org/abs/2501.11260) | Generation, planning, and prediction–planning interaction | arXiv 2025 | [Paper List](https://github.com/FengZicai/AwesomeWMAD) |

---

# Driving World Models

## Generative & Explicit-State World Models

Models that predict or generate **explicit future observations or scene states**, including RGB video, LiDAR, point clouds, occupancy, BEV, and multimodal 3D representations.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **HelloWorld** | [Towards Practical Applications of Generative Driving World Models](https://arxiv.org/abs/2609.28931) | Controllable multi-camera RGB + LiDAR generation for sequential simulation | arXiv 2026 | — |
| **Epona** | [Autoregressive Diffusion World Model for Autonomous Driving](https://arxiv.org/abs/2506.24113) | Autoregressive diffusion for long-horizon video generation and planning | ICCV 2025 | [Code](https://github.com/Kevin-thu/Epona) |
| **HERMES** | [A Unified Self-Driving World Model for Simultaneous 3D Scene Understanding and Generation](https://arxiv.org/abs/2501.14729) | Unified BEV-based scene understanding and future generation | ICCV 2025 | [Code](https://github.com/LMD0311/HERMES) |
| **InfiniCube** | [Unbounded and Controllable Dynamic 3D Driving Scene Generation with World-Guided Video Models](https://arxiv.org/abs/2412.03934) | Large-scale controllable 3D world generation grounded by video models | ICCV 2025 | [Code](https://github.com/nv-tlabs/InfiniCube) |
| **DrivingWorld** | [Constructing World Model for Autonomous Driving via Video GPT](https://arxiv.org/abs/2412.19505) | GPT-style autoregressive video and ego-state generation | arXiv 2024 | [Code](https://github.com/YvanYin/DrivingWorld) |
| **DriveDreamer-2** | [LLM-Enhanced World Models for Diverse Driving Video Generation](https://arxiv.org/abs/2403.06845) | LLM-conditioned customized multi-view driving generation | AAAI 2025 | [Project](https://drivedreamer2.github.io/) · [Code](https://github.com/f1yfisher/DriveDreamer2) |
| **LidarDM** | [Generative LiDAR Simulation in a Generated World](https://arxiv.org/abs/2404.02903) | 4D LiDAR world generation and physically grounded sensor simulation | ICRA 2025 | [Project](https://zyrianov.org/lidardm/) · [Code](https://github.com/vzyrianov/LidarDM) |
| **GenAD** | [Generalized Predictive Model for Autonomous Driving](https://arxiv.org/abs/2403.09630) | Large-scale driving video prediction with action-conditioned adaptation | CVPR 2024 | [Code](https://github.com/OpenDriveLab/DriveAGI) |
| **Drive-WM** | [Driving into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving](https://arxiv.org/abs/2311.17918) | Multi-view visual forecasting connected to trajectory planning | CVPR 2024 | [Code](https://github.com/BraveGroup/Drive-WM) |
| **WoVoGen** | [World Volume-aware Diffusion for Controllable Multi-camera Driving Scene Generation](https://arxiv.org/abs/2312.02934) | Future 4D world volume + multi-camera diffusion generation | ECCV 2024 | [Code](https://github.com/fudan-zvg/WoVoGen) |
| **OccWorld** | [Learning a 3D Occupancy World Model for Autonomous Driving](https://arxiv.org/abs/2311.16038) | Joint future 3D occupancy and ego-motion prediction | ECCV 2024 | [Code](https://github.com/wzzheng/OccWorld) |
| **MUVO** | [A Multimodal Generative World Model for Autonomous Driving with Geometric Representations](https://arxiv.org/abs/2311.11762) | Camera + LiDAR world modeling with geometric latent representations | arXiv 2023 | [Code](https://github.com/daniel-bogdoll/MUVO) |
| **Panacea** | [Panoramic and Controllable Video Generation for Autonomous Driving](https://arxiv.org/abs/2311.16813) | Controllable temporally and cross-view consistent panoramic generation | CVPR 2024 | [Project](https://panacea-ad.github.io/) · [Code](https://github.com/wenyuqing/panacea) |
| **ADriver-I** | [A General World Model for Autonomous Driving](https://arxiv.org/abs/2311.13549) | Interleaved vision-action modeling with MLLM and diffusion | arXiv 2023 | — |
| **Copilot4D** | [Learning Unsupervised World Models for Autonomous Driving via Discrete Diffusion](https://arxiv.org/abs/2311.01017) | Tokenized sensor world modeling with discrete diffusion | ICLR 2024 | — |
| **DriveDreamer** | [Towards Real-world-driven World Models for Autonomous Driving](https://arxiv.org/abs/2309.09777) | Real-world diffusion world model with structured traffic control | arXiv 2023 | [Project](https://drivedreamer.github.io/) · [Code](https://github.com/JeffWang987/DriveDreamer) |
| **GAIA-1** | [A Generative World Model for Autonomous Driving](https://arxiv.org/abs/2309.17080) | Autoregressive video, text, and action token world modeling | arXiv 2023 | [Blog](https://wayve.ai/thinking/scaling-gaia-1/) |

---

## Latent & Planning-Oriented World Models

Models that predict future states in **learned representation spaces** or explicitly use world-model predictions to improve planning, policy learning, or trajectory selection.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **ForeDrive** | [Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model](https://arxiv.org/abs/2609.26299) | JEPA-style multi-horizon latent futures directly guide a DiT planner | arXiv 2026 | — |
| **Auto-JEPA** | [A Latent World Model of Continuous Intent for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.29031) | Joint-embedding prediction of continuous future driving intent | arXiv 2026 | [Code](https://github.com/NoctYang/Auto-JEPA) |
| **GraphWorld** | [Long-Horizon Planning with World Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2606.16274) | Interaction-graph latent world states for long-horizon planning | arXiv 2026 | — |
| **DeepSight** | [Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564) | Parallel long-horizon BEV latent-state prediction | ICML 2026 | [Code](https://github.com/hotdogcheesewhite/DeepSight) |
| **DriveFuture** | [Future-Aware Latent World Models for Autonomous Driving](https://arxiv.org/abs/2605.09701) | Future-aware latent conditioning for diffusion trajectory planning | arXiv 2026 | — |
| **DriveWorld-VLA** | [Unified Latent-Space World Modeling with Vision-Language-Action for Autonomous Driving](https://arxiv.org/abs/2602.06521) | Shared latent states unify VLA planning and action-conditioned imagination | arXiv 2026 | [Code](https://github.com/liulin815/DriveWorld-VLA) |
| **World4Drive** | [End-to-End Autonomous Driving via Intention-aware Physical Latent World Model](https://arxiv.org/abs/2507.00603) | Intention-aware latent futures for trajectory generation and selection | ICCV 2025 | [Code](https://github.com/ucaszyp/World4Drive) |
| **Raw2Drive** | [Reinforcement Learning with Aligned World Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2505.16394) | Aligns privileged and raw-sensor world models for model-based RL | NeurIPS 2025 | [Code](https://github.com/Thinklab-SJTU/Raw2Drive) |
| **DriveWorld** | [4D Pre-trained Scene Understanding via World Models for Autonomous Driving](https://arxiv.org/abs/2405.04390) | Spatiotemporal latent dynamics for multi-task 4D pre-training | arXiv 2024 | — |
| **ViDAR** | [Visual Point Cloud Forecasting enables Scalable Autonomous Driving](https://arxiv.org/abs/2312.17655) | Future point-cloud forecasting as self-supervised driving pre-training | CVPR 2024 | [Code](https://github.com/OpenDriveLab/ViDAR) |
| **Think2Drive** | [Efficient Reinforcement Learning by Thinking in Latent World Model for Quasi-Realistic Autonomous Driving](https://arxiv.org/abs/2402.16720) | Latent imagination for model-based reinforcement learning | arXiv 2024 | — |
| **UniWorld** | [Autonomous Driving Pre-training via World Models](https://arxiv.org/abs/2308.07234) | Label-free 4D occupancy prediction for transferable driving pre-training | arXiv 2023 | [Code](https://github.com/chaytonmin/UniWorld) |
| **TrafficBots** | [Towards World Models for Autonomous Driving Simulation and Motion Prediction](https://arxiv.org/abs/2303.04116) | Multi-agent world model for configurable traffic simulation and prediction | ICRA 2023 | [Code](https://github.com/zhejz/TrafficBots) |
| **MILE** | [Model-Based Imitation Learning for Urban Driving](https://proceedings.neurips.cc/paper_files/paper/2022/hash/827cb489449ea216e4a257c47e407d18-Abstract-Conference.html) | Joint latent world model and policy learned from offline driving video | NeurIPS 2022 | [Code](https://github.com/wayveai/mile) |

---

## World-Action & Action-Aligned Models

Models that explicitly connect future-world modeling with actions, either through **joint prediction** or by aligning action representations with learned world states.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **MM-Future** | [Multi-Mode Joint World-Action Modeling for Autonomous Driving](https://arxiv.org/abs/2609.20377) | Multiple paired scene-action futures with joint diffusion modeling | arXiv 2026 | — |
| **WALT** | [Learning World-Model-Aligned Latent Trajectories for Autonomous Driving](https://arxiv.org/abs/2609.30436) | Transfers world-model semantics into compact trajectory latents | arXiv 2026 | — |
| **WA-JEPA** | [Rethinking the Video JEPA Paradigm for World-Action Modeling in Autonomous Driving](https://arxiv.org/abs/2608.20974) | Future-masked JEPA + latent flow matching + joint world-action prediction | arXiv 2026 | [Project](https://wa-jepa.github.io/) · [Code](https://github.com/AFARI-Research/WA-JEPA) |
| **DA-WAM** | [Decision-Aligned Future Latents for Driving World Models](https://arxiv.org/abs/2608.19085) | Action-conditioned future latents optimized for trajectory scoring | arXiv 2026 | — |

---

# Driving Representation Learning

## JEPA-based Methods

Predictive representation-learning methods relevant to driving world models but not necessarily designed as complete temporal world models.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **AD-L-JEPA** | [Self-Supervised Spatial World Models with Joint Embedding Predictive Architecture for Autonomous Driving with LiDAR Data](https://arxiv.org/abs/2501.04969) | JEPA-based BEV LiDAR representation pre-training | arXiv 2025 | [Project](https://ad-l-jepa.github.io/) · [Code](https://github.com/DZY122/AD-L-JEPA-Release) |

---

# Related Work

Selected papers outside the main autonomous-driving world-model taxonomy that introduce directly relevant ideas for **joint world-action prediction**, **controllable future generation**, or **embodied world modeling**.

## Embodied / Robotics World Models

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **XPACE** | [Joint World and Action Modeling from Heterogeneous Experience](https://arxiv.org/abs/2609.17372) | Shared video backbone jointly predicts robot actions and future video | arXiv 2026 | [Project](https://xpeng-robotics.github.io/xpace/) |

---

## General Video World Models

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **Holo-World** | [Unified Camera, Object and Weather Control for Video World Model](https://arxiv.org/abs/2606.20083) | Unified camera, object, and weather control from a single source image | arXiv 2026 | [Project](https://xiangchenyin.github.io/Holo-World/) · [Code](https://github.com/XiangchenYin/Holo-World) |

<!-- PAPERS_END -->

---

# Recent Updates

- **2026-09-30** — Expanded the repository from an initial recent-paper list into a broader research map covering foundational, generative, latent, planning-oriented, world-action, and JEPA-based driving world models.
- **2026-09-29** — Initialized the curated paper list with structured metadata and categorized recent work on driving world models.

---

# Concepts

### Generative / Explicit-State World Model

Predicts or generates future observations or explicit scene representations, such as **RGB video, LiDAR, point clouds, BEV states, or occupancy**.

### Latent World Model

Models future evolution in a **learned representation space** rather than reconstructing every detail of the raw observation.

### Planning-Oriented World Model

Learns future representations specifically to support **trajectory generation, evaluation, policy learning, or closed-loop decision making**.

### World-Action Model

Models **future world states and agent actions together**, allowing predicted scene evolution and action generation to influence each other.

### JEPA

**Joint-Embedding Predictive Architecture** learns by predicting target representations in embedding space rather than reconstructing raw observations.

JEPA-style learning can be used for:

- spatial representation pre-training,
- temporal future prediction,
- planning-relevant latent modeling,
- or joint world-action prediction.

### E2E Driving

**End-to-End autonomous driving** maps sensory observations and optional context directly to planning or control outputs with a learned model.

---

# Contributing

Contributions are welcome.

Paper metadata is maintained in:

```text
data/papers.yaml
```

The paper tables in this README are generated automatically.

To add or update a paper:

1. Edit the corresponding entry in `data/papers.yaml`.
2. Regenerate the README:

```bash
pip install -r requirements.txt
python scripts/generate_readme.py
```

3. Check the generated tables and links.
4. Open a pull request.

The generation script should only modify content between:

```text
<!-- PAPERS_START -->
<!-- PAPERS_END -->
```

Everything outside these markers can be edited manually.

### Suggested metadata for each paper

```yaml
- model:
  title:
  paper:
  year:
  venue:
  category:
  focus:
  code:
  project:
```

Please provide as much of the following information as possible:

- model / method name,
- paper title,
- paper URL,
- publication year,
- venue,
- category,
- one-line description of the key idea,
- code repository,
- project page.

---

# Repository Structure

```text
.
├── README.md
├── data/
│   └── papers.yaml
├── scripts/
│   └── generate_readme.py
└── requirements.txt
```

---

# Inclusion Criteria

A paper is generally included when it makes a clear contribution to at least one of the following:

- future environment or scene prediction for autonomous driving,
- learned world dynamics,
- RGB / video / LiDAR / occupancy / BEV future generation,
- latent future-state prediction,
- self-supervised predictive world representation learning,
- model-based imitation or reinforcement learning for driving,
- future-conditioned trajectory planning,
- action-conditioned world prediction,
- joint world-action modeling,
- world-model-aligned action or trajectory representations.

The repository intentionally does **not** aim to cover every paper in:

- autonomous-driving perception,
- generic trajectory prediction,
- general VLM / VLA driving,
- generic video generation,
- or conventional planning.

Those works are included only when **world modeling or predictive future representation is central to the method**.

---

# Acknowledgements

This repository is intended as a continuously updated research index for the rapidly evolving area of **driving world models**.

If you find a missing paper, incorrect metadata, broken link, or a better way to categorize a method, issues and pull requests are welcome.

⭐ If you find this repository useful, consider giving it a star.
