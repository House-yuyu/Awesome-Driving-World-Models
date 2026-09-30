# Awesome Driving World Models 🚗🌎

<p align="center">
  <img src="https://img.shields.io/badge/papers-71-blue" alt="Papers">
  <img src="https://img.shields.io/badge/last%20updated-2026--09--30-brightgreen" alt="Last Updated">
  <img src="https://img.shields.io/badge/PRs-welcome-orange" alt="PRs Welcome">
  <img src="https://visitor-badge.laobi.icu/badge?page_id=House-yuyu.Awesome-Driving-World-Models" alt="Visitors">
</p>

A curated collection of research on **world models for autonomous driving**, spanning **generative simulation**, **explicit-state prediction**, **latent future modeling**, **world-action modeling**, and two rapidly growing cross-cutting directions: **JEPA for driving** and **Vision-Language-Action (VLA) models with world modeling**.

> **From predicting observations to learning decision-relevant futures, actions, and world-aware policies.**


---

## Scope

The collection is organized primarily by **what the model predicts and how that prediction is used**.

```text
Core Driving World Models
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
└── World-Action & Action-Aligned Models
    ├── joint future-world / action prediction
    ├── video-action policies
    └── world-model-aligned action representations

Cross-Cutting Directions
├── JEPA for Autonomous Driving
│   ├── representation pre-training
│   ├── latent world modeling
│   ├── planning
│   └── world-action modeling
│
└── Vision-Language-Action (VLA) for Driving
    ├── world-model-enhanced VLA
    └── selected general driving VLA

Related Work
├── Embodied / Robotics World Models
└── General Video World Models
```

### What is included?

A paper is generally included when at least one of the following is central to the method:

- future-world prediction,
- learned environment dynamics,
- latent future modeling,
- action-conditioned world prediction,
- world-action coupling,
- predictive representation learning for driving,
- or world modeling used to improve VLA/VLM planning.

General perception, planning, VLM/VLA, or video-generation papers are not included in the core tables unless they have a clear connection to world modeling. A small **Selected General Driving VLA** section is retained as context for the VLA direction.

---

## Contents

- [Surveys & Perspectives](#surveys--perspectives)
- [Driving World Models](#driving-world-models)
  - [Generative & Explicit-State World Models](#generative--explicit-state-world-models)
  - [Latent & Planning-Oriented World Models](#latent--planning-oriented-world-models)
  - [World-Action & Action-Aligned Models](#world-action--action-aligned-models)
- [JEPA for Autonomous Driving](#jepa-for-autonomous-driving)
- [Vision-Language-Action for Driving](#vision-language-action-for-driving)
  - [World-Model-Enhanced VLA](#world-model-enhanced-vla)
  - [Selected General Driving VLA](#selected-general-driving-vla)
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
| **AV JEPA Survey** | [Joint Embedding Predictive Architecture for Autonomous Vehicle Safety and Security: A Comprehensive Survey](https://www.sciencedirect.com/science/article/pii/S1474034626002909) | JEPA for autonomous-vehicle perception, safety, security, and deployment | Advanced Engineering Informatics 2026 | — |
| **DWM Survey** | [The Role of World Models in Shaping Autonomous Driving: A Comprehensive Survey](https://arxiv.org/abs/2502.10498) | Driving world models by predicted scene modality | arXiv 2025 | [Paper List](https://github.com/LMD0311/Awesome-World-Model) |
| **VLA4AD Survey** | [A Survey on Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2506.24044) | Driving VLA architectures, datasets, evaluation, and research trends | ICCV Workshops 2025 | [Paper List](https://github.com/JohnsonJiang1996/Awesome-VLA4AD) |
| **WMAD Survey** | [A Survey of World Models for Autonomous Driving](https://arxiv.org/abs/2501.11260) | Generation, planning, and prediction–planning interaction | arXiv 2025 | [Paper List](https://github.com/FengZicai/AwesomeWMAD) |

---

# Driving World Models

## Generative & Explicit-State World Models

Models that predict or generate **explicit future observations or scene states**, including RGB video, LiDAR, point clouds, occupancy, BEV, and multimodal 3D representations.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **HelloWorld** | [Towards Practical Applications of Generative Driving World Models](https://arxiv.org/abs/2609.28931) | Controllable multi-camera RGB + LiDAR generation for sequential simulation | arXiv 2026 | [Project](https://helloworld-4d.github.io/) |
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

> JEPA-based methods are intentionally collected in the dedicated [JEPA for Autonomous Driving](#jepa-for-autonomous-driving) section rather than duplicated here.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **DriveLaW** | [Unifying Planning and Video Generation in a Latent Driving World](https://arxiv.org/abs/2512.23421) | Video-world latents are directly injected into a diffusion planner | CVPR 2026 | [Code](https://github.com/xiaomi-research/drivelaw) |
| **GraphWorld** | [Long-Horizon Planning with World Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2606.16274) | Interaction-graph latent world states for long-horizon planning | arXiv 2026 | — |
| **DeepSight** | [Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564) | Parallel long-horizon BEV latent-state prediction | ICML 2026 | [Code](https://github.com/hotdogcheesewhite/DeepSight) |
| **DriveFuture** | [Future-Aware Latent World Models for Autonomous Driving](https://arxiv.org/abs/2605.09701) | Future-aware latent conditioning for diffusion trajectory planning | arXiv 2026 | — |
| **World4Drive** | [End-to-End Autonomous Driving via Intention-aware Physical Latent World Model](https://arxiv.org/abs/2507.00603) | Intention-aware latent futures for trajectory generation and selection | ICCV 2025 | [Code](https://github.com/ucaszyp/World4Drive) |
| **Raw2Drive** | [Reinforcement Learning with Aligned World Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2505.16394) | Aligns privileged and raw-sensor world models for model-based RL | NeurIPS 2025 | [Code](https://github.com/Thinklab-SJTU/Raw2Drive) |
| **DriveWorld** | [4D Pre-trained Scene Understanding via World Models for Autonomous Driving](https://arxiv.org/abs/2405.04390) | Spatiotemporal latent dynamics for multi-task 4D pre-training | arXiv 2024 | — |
| **ViDAR** | [Visual Point Cloud Forecasting Enables Scalable Autonomous Driving](https://arxiv.org/abs/2312.17655) | Future point-cloud forecasting as self-supervised driving pre-training | CVPR 2024 | [Code](https://github.com/OpenDriveLab/ViDAR) |
| **Think2Drive** | [Efficient Reinforcement Learning by Thinking in Latent World Model for Quasi-Realistic Autonomous Driving](https://arxiv.org/abs/2402.16720) | Latent imagination for model-based reinforcement learning | arXiv 2024 | — |
| **UniWorld** | [Autonomous Driving Pre-training via World Models](https://arxiv.org/abs/2308.07234) | Label-free 4D occupancy prediction for transferable driving pre-training | arXiv 2023 | [Code](https://github.com/chaytonmin/UniWorld) |
| **TrafficBots** | [Towards World Models for Autonomous Driving Simulation and Motion Prediction](https://arxiv.org/abs/2303.04116) | Multi-agent world model for configurable traffic simulation and prediction | ICRA 2023 | [Code](https://github.com/zhejz/TrafficBots) |
| **MILE** | [Model-Based Imitation Learning for Urban Driving](https://proceedings.neurips.cc/paper_files/paper/2022/hash/827cb489449ea216e4a257c47e407d18-Abstract-Conference.html) | Joint latent world model and policy learned from offline driving video | NeurIPS 2022 | [Code](https://github.com/wayveai/mile) |

---

## World-Action & Action-Aligned Models

Models that explicitly connect future-world modeling with actions, either through **joint prediction**, **video-action policies**, or **action representations aligned with learned world states**.

> WA-JEPA is listed in the dedicated JEPA section below.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **WALT** | [Learning World-Model-Aligned Latent Trajectories for Autonomous Driving](https://arxiv.org/abs/2609.30436) | Transfers world-model semantics into compact trajectory latents | arXiv 2026 | — |
| **MM-Future** | [Multi-Mode Joint World-Action Modeling for Autonomous Driving](https://arxiv.org/abs/2609.20377) | Multiple paired scene-action futures with joint diffusion modeling | arXiv 2026 | — |
| **GeoWAM** | [Visual Geometry World Action Models for Autonomous Driving](https://arxiv.org/abs/2608.23486) | Predicts future scene geometry and conditions ego actions on geometric dynamics | arXiv 2026 | — |
| **DA-WAM** | [Decision-Aligned Future Latents for Driving World Models](https://arxiv.org/abs/2608.19085) | Action-conditioned future latents optimized for trajectory scoring | arXiv 2026 | — |
| **SimWAM** | [A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468) | Uses future-video prediction as training-only supervision for an efficient action expert | arXiv 2026 | [Code](https://github.com/H-EmbodVis/SimWAM) |
| **DriveWAM** | [Video Generative Priors Enable Scalable World-Action Modeling for Autonomous Driving](https://arxiv.org/abs/2605.28544) | Adapts a video diffusion transformer into an autoregressive video-action policy | arXiv 2026 | [Project](https://chenshi3.github.io/drivewam.github.io/) · [Code](https://github.com/chenshi3/DriveWAM) |
| **Latent-WAM** | [Latent World Action Modeling for End-to-End Autonomous Driving](https://arxiv.org/abs/2603.24581) | Compact spatial world tokens + causal latent dynamics for action planning | arXiv 2026 | — |

---

# JEPA for Autonomous Driving

All driving-related JEPA papers are collected here **in one place**, even when their downstream role differs substantially.

The track now spans a progression from **LiDAR representation learning → video pre-training → latent intent prediction → planning-relevant future prediction → world-action modeling → action-conditioned JEPA world models for zero-shot planning**.

| Model | Paper | Driving Role | Venue | Resources |
| --- | --- | --- | --- | --- |
| **AD-E2E-JEPA** | [A Joint-Embedding Predictive Architecture for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.34085) | Action-conditioned JEPA world model for efficient goal-conditioned zero-shot planning and downstream IL | arXiv 2026 | [Code](https://github.com/HaoranZhuExplorer/AD-E2E-JEPA) |
| **ForeDrive** | [Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model](https://arxiv.org/abs/2609.26299) | JEPA-style multi-horizon latent futures directly condition a DiT planner | arXiv 2026 | — |
| **WA-JEPA** | [Rethinking the Video JEPA Paradigm for World-Action Modeling in Autonomous Driving](https://arxiv.org/abs/2608.20974) | Future-masked V-JEPA + flow matching + joint future-scene / action prediction | arXiv 2026 | [Project](https://wa-jepa.github.io/) · [Code](https://github.com/AFARI-Research/WA-JEPA) |
| **Auto-JEPA** | [A Latent World Model of Continuous Intent for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.29031) | Predicts planning-relevant continuous future-intent embeddings instead of dense future scenes | arXiv 2026 | [Code](https://github.com/NoctYang/Auto-JEPA) |
| **Drive-JEPA** | [Video JEPA Meets Multimodal Trajectory Distillation for End-to-End Driving](https://arxiv.org/abs/2601.22032) | V-JEPA video pre-training aligned with proposal-based end-to-end planning | arXiv 2026 | [Code](https://github.com/linhanwang/Drive-JEPA) |
| **HanoiWorld** | [A Joint Embedding Predictive Architecture Based World Model for Autonomous Vehicle Controller](https://arxiv.org/abs/2601.01577) | JEPA-based recurrent world model for long-horizon autonomous-vehicle control | arXiv 2026 | — |
| **LM-JEPA** | [Object Detection and Scene Perception for Connected and Autonomous Vehicles Using LM-JEPA](https://www.mdpi.com/1424-8220/26/15/4894) | Latent predictive representation learning for resource-efficient connected-vehicle perception | Sensors 2026 | — |
| **AD-L-JEPA** | [Self-Supervised Representation Learning with Joint Embedding Predictive Architecture for Automotive LiDAR Object Detection](https://arxiv.org/abs/2501.04969) | BEV LiDAR representation pre-training for downstream 3D detection | AAAI 2026 | [Project](https://ad-l-jepa.github.io/) · [Code](https://github.com/HaoranZhuExplorer/adljepa) |

---

# Vision-Language-Action for Driving

This section tracks the growing intersection between **VLA/VLM planning** and **world modeling**.

To keep the repository focused, the first subsection contains papers where world prediction or world representation is a **central mechanism**. The second subsection contains a selected set of broader driving VLA papers that provide useful architectural or data context.

## World-Model-Enhanced VLA

| Model | Paper | World-Model / Reasoning Mechanism | Venue | Resources |
| --- | --- | --- | --- | --- |
| **HyWorldVLA** | [A Vision-Language-Action Model with Hybrid World Modeling for Autonomous Driving](https://arxiv.org/abs/2607.20988) | Combines pixel-level grounding with latent future prediction before action generation | arXiv 2026 | — |
| **WCog-VLA** | [A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.08375) | Semantic world cognition + generative joint multi-agent future modeling + Game-CoT | arXiv 2026 | — |
| **LWDrive** | [Layer-Wise World-Model-Guided Vision-Language Model Planning for Autonomous Driving](https://arxiv.org/abs/2606.29879) | Future-frame supervision shapes VLM hidden states for coarse-to-fine trajectory refinement | arXiv 2026 | [Code](https://github.com/yachyc/LWDrive) |
| **CoWorld-VLA** | [Thinking in a Multi-Expert World Model for Autonomous Driving](https://arxiv.org/abs/2605.10426) | Multi-expert world tokens for semantics, geometry, dynamics, and ego goals explicitly condition planning | arXiv 2026 | [Code](https://github.com/AFARI-Research/CoWorld-VLA) |
| **VLA-World** | [Learning Vision-Language-Action World Models for Autonomous Driving](https://arxiv.org/abs/2604.09059) | Generates an action-guided future image, then reasons over the imagined future to refine the trajectory | arXiv 2026 | [Project](https://vlaworld.github.io/) |
| **OneVL** | [One-Step Latent Reasoning and Planning with Vision-Language Explanation](https://arxiv.org/abs/2604.18486) | Compact latent CoT is jointly supervised by language reasoning and a visual future-world decoder | arXiv 2026 | [Code](https://github.com/xiaomi-research/onevl) |
| **ExploreVLA** | [Dense World Modeling and Exploration for End-to-End Autonomous Driving](https://arxiv.org/abs/2604.02714) | Uses world-model uncertainty as an intrinsic reward for safe exploration | ECCV 2026 | [Code](https://github.com/zihaosheng/ExploreVLA) |
| **Uni-World VLA** | [Interleaved World Modeling and Planning for Autonomous Driving](https://arxiv.org/abs/2603.27287) | Alternates future-frame prediction and ego-action generation in one autoregressive sequence | arXiv 2026 | [Code](https://github.com/LogosRoboticsGroup/UniWorldVLA) |
| **DynVLA** | [Learning World Dynamics for Action Reasoning in Autonomous Driving](https://arxiv.org/abs/2603.11041) | Dynamics CoT compresses ego- and environment-centric future evolution into compact dynamics tokens | ICML 2026 | [Project](https://yaoyao-jpg.github.io/dynvla/) · [Code](https://github.com/yaoyao-jpg/DynamicsVLA) |
| **DriveWorld-VLA** | [Unified Latent-Space World Modeling with Vision-Language-Action for Autonomous Driving](https://arxiv.org/abs/2602.06521) | Shared latent world states support action-conditioned imagination and VLA planning | arXiv 2026 | [Code](https://github.com/liulin815/DriveWorld-VLA) |
| **DriveVLA-W0** | [World Models Amplify Data Scaling Law in Autonomous Driving](https://arxiv.org/abs/2510.12796) | Future-image world modeling supplies dense self-supervision for VLA scaling | ICLR 2026 | [Code](https://github.com/BraveGroup/DriveVLA-W0) |
| **DriveVLA-M0** | [Failure-Aware Memory Augmentation for Autonomous Driving](https://arxiv.org/abs/2608.10413) | Failure-aware latent memory with structurally grounded retrieval and lightweight test-time adaptation | ACM MM 2026 | [Code](https://github.com/ZebinX/DriveVLA-M0) |
| **FutureSightDrive** | [Thinking Visually with Spatio-Temporal CoT for Autonomous Driving](https://arxiv.org/abs/2505.17685) | VLA first acts as a world model to generate a visual future CoT, then plans from it | NeurIPS 2025 | [Project](https://miv-xjtu.github.io/FSDrive.github.io/) · [Code](https://github.com/MIV-XJTU/FSDrive) |

---

## Selected General Driving VLA

These papers are not necessarily world models themselves, but they are useful reference points for understanding the broader VLA-for-driving trajectory.

| Model | Paper | Main Focus | Venue | Resources |
| --- | --- | --- | --- | --- |
| **MindVLA-U1** | [VLA Beats VA with Unified Streaming Architecture for Autonomous Driving](https://arxiv.org/abs/2605.12624) | Unified streaming language + continuous-action generation with memory | arXiv 2026 | [Project](https://mind-omni.github.io/projects/u1/index.html) |
| **OneDrive** | [Unified Multi-Paradigm Driving with Vision-Language-Action Models](https://arxiv.org/abs/2604.17915) | One causal VLM decoder for language, perception queries, and trajectory queries | arXiv 2026 | [Code](https://github.com/Z1zyw/OneDrive) |
| **UniDriveVLA** | [Unifying Understanding, Perception, and Action Planning for Autonomous Driving](https://arxiv.org/abs/2604.02190) | Mixture-of-Transformers experts for semantic reasoning, spatial perception, and planning | arXiv 2026 | [Code](https://github.com/xiaomi-research/unidrivevla) |
| **OpenDriveVLA** | [Towards End-to-End Autonomous Driving with Large Vision Language Action Model](https://arxiv.org/abs/2503.23463) | 2D/3D vision-language alignment with agent–environment–ego interaction modeling | AAAI 2026 | [Project](https://drivevla.github.io/) · [Code](https://github.com/DriveVLA/OpenDriveVLA) |
| **Reasoning-VLA** | [A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving](https://arxiv.org/abs/2511.19912) | Parallel continuous action generation from reasoning-enhanced VLM features | arXiv 2025 | — |
| **AutoVLA** | [A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning](https://arxiv.org/abs/2506.13757) | Adaptive fast/slow CoT reasoning with physical action tokens and GRPO fine-tuning | NeurIPS 2025 | [Project](https://autovla.github.io/) · [Code](https://github.com/ucla-mobility/AutoVLA) |
| **Impromptu VLA** | [Open Weights and Open Data for Driving Vision-Language-Action Models](https://arxiv.org/abs/2505.23757) | Large open corner-case VLA dataset, benchmark, weights, and planning-oriented QA | NeurIPS 2025 | [Project](https://ziming-liu.github.io/projects/impromptu-vla/index.html) · [Code](https://github.com/ahydchh/Impromptu-VLA) |

---

# Related Work

Selected papers outside the main autonomous-driving taxonomy that introduce ideas directly relevant to **joint world-action prediction**, **controllable future generation**, or **embodied world modeling**.

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

- **2026-09-30** — Reorganized all driving-related JEPA work into one dedicated section; added **AD-E2E-JEPA** and additional JEPA-for-driving papers.
- **2026-09-30** — Added a dedicated **Vision-Language-Action for Driving** track, including **CoWorld-VLA**, DriveWorld-VLA, DynVLA, Uni-World VLA, VLA-World, OneVL, HyWorldVLA, WCog-VLA, and related VLA references.
- **2026-09-30** — Expanded the World-Action section with DriveWAM, Latent-WAM, SimWAM, and GeoWAM.
- **2026-09-30** — Expanded the repository from an initial recent-paper list into a broader research map covering foundational, generative, latent, planning-oriented, world-action, JEPA, and VLA directions.
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

Models **future world states and agent actions together**, or transfers a learned world-dynamics prior directly into an action policy.

### JEPA

**Joint-Embedding Predictive Architecture** learns by predicting target representations in embedding space rather than reconstructing raw observations.

For driving, JEPA-style learning now spans:

- LiDAR / BEV representation pre-training,
- video representation learning,
- future latent prediction,
- continuous intent prediction,
- planning-relevant world modeling,
- world-action modeling,
- and action-conditioned world-model rollout for planning.

### Vision-Language-Action (VLA)

A **Vision-Language-Action** model combines visual observations and language-level semantic reasoning with direct action or trajectory prediction.

### World-Model-Enhanced VLA

A VLA in which future-world prediction or world-state representations are used as a central component of reasoning or planning, for example through:

- future image generation,
- latent future prediction,
- dynamics tokens,
- world/cognitive expert tokens,
- imagined future-frame reasoning,
- or explicit world-model uncertainty.

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

Recommended `category` values:

```text
survey
generative
latent
world-action
jepa
vla-world
vla-general
related-embodied
related-video
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

A paper is generally included in the **core world-model sections** when it makes a clear contribution to at least one of the following:

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

The **JEPA** section intentionally includes driving-related JEPA methods across perception, representation learning, world modeling, and planning so that the full development line can be viewed in one place.

The **World-Model-Enhanced VLA** section includes VLA/VLM methods where future prediction or learned world representations materially participate in reasoning or action generation.

The **Selected General Driving VLA** section is intentionally selective. It provides architectural and dataset context without turning this repository into a complete VLA bibliography.

The repository does **not** aim to cover every paper in:

- autonomous-driving perception,
- generic trajectory prediction,
- all VLM / VLA driving,
- generic video generation,
- or conventional planning.

---

# Acknowledgements

This repository is intended as a continuously updated research index for the rapidly evolving area of **driving world models** and their convergence with **JEPA**, **world-action models**, and **driving VLA**.

If you find a missing paper, incorrect metadata, broken link, or a better way to categorize a method, issues and pull requests are welcome.

⭐ If you find this repository useful, consider giving it a star.
