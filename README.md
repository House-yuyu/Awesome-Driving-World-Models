# Awesome Driving World Models 🚗🌎

<p align="center">
  <img src="https://img.shields.io/badge/papers-112-blue" alt="Papers">
  <img src="https://img.shields.io/badge/last%20updated-2026--10--19-brightgreen" alt="Last Updated">
  <img src="https://img.shields.io/badge/PRs-welcome-orange" alt="PRs Welcome">
  <img src="https://visitor-badge.laobi.icu/badge?page_id=House-yuyu.Awesome-Driving-World-Models" alt="Visitors">
</p>

A curated collection of research on **world models for autonomous driving**, spanning **generative simulation**, **explicit-state prediction**, **latent future modeling**, **world-action modeling**, and two rapidly growing cross-cutting directions: **JEPA for driving** and **Vision-Language-Action (VLA) models with world modeling**.

> **From predicting observations to learning decision-relevant futures, actions, and world-aware policies.**

Paper tables are sorted by publication year, then by first-posted date when available. **arXiv** denotes the indexed preprint version; **accepted** marks a confirmed acceptance before final publication. **Code** links to an available implementation, **Repository** to an informational or unreleased repository, and **Data** to dataset tools. Resource availability was checked on **October 19, 2026**.

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
- [Benchmarks & Simulation](#benchmarks--simulation)
- [Related Work](#related-work)
  - [Embodied / Robotics World Models](#embodied--robotics-world-models)
  - [General Video World Models](#general-video-world-models)
- [Datasets & Toolkits](#datasets--toolkits)
- [Industrial World Models](#industrial-world-models)
- [Recent Updates](#recent-updates)
- [Concepts](#concepts)
- [Contributing](#contributing)
- [Repository Structure](#repository-structure)
- [Inclusion Criteria](#inclusion-criteria)

---

<!-- PAPERS_START -->

# Surveys & Perspectives

Driving-focused reviews and selected broader perspectives on predictive, controllable, and actionable world models.

| Work | Paper | Focus | Venue | Resources |
| --- | --- | --- | --- | --- |
| **Embodied WM Survey** | [World Models for Embodied Intelligence: From Plausible to Controllable to Actionable](https://arxiv.org/abs/2609.16697) | Capability hierarchy from plausible prediction to controllable and actionable embodied models | arXiv 2026 | — |
| **Latent WM Survey** | [Latent World Models for Automated Driving: A Unified Taxonomy, Evaluation Framework, and Open Challenges](https://arxiv.org/abs/2603.09086) | Latent-state taxonomy, evaluation, and deployment challenges | arXiv 2026 | — |
| **DWM Survey** | [The Role of World Models in Shaping Autonomous Driving: A Comprehensive Survey](https://arxiv.org/abs/2502.10498) | Driving world models by predicted scene modality | [Frontiers of Computer Science 2026 (accepted)](https://journal.hep.com.cn/fcs/EN/10.1007/s11704-026-60102-1) | [Paper List](https://github.com/LMD0311/Awesome-World-Model) |
| **AV JEPA Survey** | [Joint Embedding Predictive Architecture for Autonomous Vehicle Safety and Security: A Comprehensive Survey](https://www.sciencedirect.com/science/article/pii/S1474034626002909) | JEPA for autonomous-vehicle perception, safety, security, and deployment | Advanced Engineering Informatics 2026 | — |
| **VLA4AD Survey** | [A Survey on Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2506.24044) | Driving VLA architectures, datasets, evaluation, and research trends | ICCV Workshops 2025 | [Paper List](https://github.com/JohnsonJiang1996/Awesome-VLA4AD) |
| **WMAD Survey** | [A Survey of World Models for Autonomous Driving](https://arxiv.org/abs/2501.11260) | Generation, planning, and prediction–planning interaction | arXiv 2025 | [Paper List](https://github.com/FengZicai/AwesomeWMAD) |

---

# Driving World Models

Generative, latent, and world-action approaches for autonomous driving.

## Generative & Explicit-State World Models

Models that predict or generate explicit future observations or scene states: RGB video, LiDAR, occupancy, BEV, and 3D geometry.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **InfraWorld** | [InfraWorld: Motion-Aware World Modeling for Roadside 4D Occupancy Forecasting](https://arxiv.org/abs/2610.14544) | Dense BEV states and persistent motion queries forecast roadside 4D occupancy | arXiv 2026 | — |
| **GeoWM** | [GeoWM: Efficient Direct World Modeling in Explicit Geometry](https://arxiv.org/abs/2610.07381) | Flow matching directly forecasts explicit future geometry at requested horizons | arXiv 2026 | — |
| **CoDrive** | [CoDrive: Cross-Vehicle World-Consistent Video Generation with Precise Trajectory Control for Cooperative Driving](https://arxiv.org/abs/2609.34749) | Shared world coordinates and cross-vehicle attention maintain multi-agent video consistency | arXiv 2026 | — |
| **ZYT-World** | [ZYT-World: A Real-Time Controllable World Model for Closed-Loop Autonomous-Driving Simulation](https://arxiv.org/abs/2609.21712) | Streaming mixed fisheye-pinhole video generation supports action control and revisitation memory | arXiv 2026 | [Project](https://zyt-aim.github.io/ZYT-World/) |
| **CausalDrive** | [CausalDrive: Real-time Causal World Models for Autonomous Driving](https://arxiv.org/abs/2606.15341) | Text and ego actions drive reactive future generation without oracle background trajectories | arXiv 2026 | — |
| **HelloWorld** | [HelloWorld: Towards Practical Applications of Generative Driving World Models](https://arxiv.org/abs/2609.28931) | Controllable multi-camera RGB + LiDAR generation for sequential simulation | arXiv 2026 | [Project](https://helloworld-4d.github.io/) |
| **Epona** | [Epona: Autoregressive Diffusion World Model for Autonomous Driving](https://arxiv.org/abs/2506.24113) | Autoregressive diffusion for long-horizon video generation and planning | ICCV 2025 | [Code](https://github.com/Kevin-thu/Epona) |
| **ReSim** | [ReSim: Reliable World Simulation for Autonomous Driving](https://arxiv.org/abs/2506.09981) | Expert and non-expert data improve action-faithful driving simulation and video-based rewards | [NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f502981cbe221d857ad409450a7917c3-Abstract-Conference.html) | [Code](https://github.com/OpenDriveLab/ReSim) · [Project](https://opendrivelab.com/ReSim) |
| **GAIA-2** | [GAIA-2: A Controllable Multi-View Generative World Model for Autonomous Driving](https://arxiv.org/abs/2503.20523) | Latent diffusion jointly controls ego motion, agents, environment, and consistent camera views | arXiv 2025 | [Project](https://wayve.ai/thinking/gaia-2/) |
| **MaskGWM** | [MaskGWM: A Generalizable Driving World Model with Video Mask Reconstruction](https://arxiv.org/abs/2502.11663) | Spatial-temporal masked reconstruction improves diffusion-transformer driving video prediction | [CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Ni_MaskGWM_A_Generalizable_Driving_World_Model_with_Video_Mask_Reconstruction_CVPR_2025_paper.html) | [Code](https://github.com/SenseTime-FVG/OpenDWM) |
| **HERMES** | [HERMES: A Unified Self-Driving World Model for Simultaneous 3D Scene Understanding and Generation](https://arxiv.org/abs/2501.14729) | Unified BEV-based scene understanding and future generation | ICCV 2025 | [Code](https://github.com/LMD0311/HERMES) |
| **InfiniCube** | [InfiniCube: Unbounded and Controllable Dynamic 3D Driving Scene Generation with World-Guided Video Models](https://arxiv.org/abs/2412.03934) | Large-scale controllable 3D world generation grounded by video models | ICCV 2025 | [Code](https://github.com/nv-tlabs/InfiniCube) |
| **LidarDM** | [LidarDM: Generative LiDAR Simulation in a Generated World](https://arxiv.org/abs/2404.02903) | 4D LiDAR world generation and physically grounded sensor simulation | ICRA 2025 | [Code](https://github.com/vzyrianov/LidarDM) · [Project](https://zyrianov.org/lidardm/) |
| **DriveDreamer-2** | [DriveDreamer-2: LLM-Enhanced World Models for Diverse Driving Video Generation](https://arxiv.org/abs/2403.06845) | LLM-conditioned customized multi-view driving generation | AAAI 2025 | [Code](https://github.com/f1yfisher/DriveDreamer2) · [Project](https://drivedreamer2.github.io/) |
| **MUVO** | [MUVO: A Multimodal Generative World Model for Autonomous Driving with Geometric Representations](https://arxiv.org/abs/2311.11762) | Camera + LiDAR world modeling with geometric latent representations | IEEE IV 2025 | [Code](https://github.com/daniel-bogdoll/MUVO) |
| **DrivingWorld** | [DrivingWorld: Constructing World Model for Autonomous Driving via Video GPT](https://arxiv.org/abs/2412.19505) | GPT-style autoregressive video and ego-state generation | arXiv 2024 | [Code](https://github.com/YvanYin/DrivingWorld) (partial) |
| **DOME** | [DOME: Taming Diffusion Model into High-Fidelity Controllable Occupancy World Model](https://arxiv.org/abs/2410.10429) | Trajectory-conditioned diffusion forecasts detailed long-horizon 3D occupancy | arXiv 2024 | [Code](https://github.com/gusongen/DOME) · [Project](https://gusongen.github.io/DOME/) |
| **Vista** | [Vista: A Generalizable Driving World Model with High Fidelity and Versatile Controllability](https://arxiv.org/abs/2405.17398) | Controllable driving-video rollouts generalize across scenes and provide visual reward signals | NeurIPS 2024 | [Code](https://github.com/OpenDriveLab/Vista) · [Project](https://vista-demo.github.io/) |
| **GenAD** | [GenAD: Generalized Predictive Model for Autonomous Driving](https://arxiv.org/abs/2403.09630) | Large-scale driving video prediction with action-conditioned adaptation | CVPR 2024 | [Data](https://github.com/OpenDriveLab/DriveAGI) |
| **WoVoGen** | [WoVoGen: World Volume-aware Diffusion for Controllable Multi-camera Driving Scene Generation](https://arxiv.org/abs/2312.02934) | Future 4D world volume + multi-camera diffusion generation | ECCV 2024 | [Code](https://github.com/fudan-zvg/WoVoGen) |
| **Drive-WM** | [Driving into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving](https://arxiv.org/abs/2311.17918) | Multi-view visual forecasting connected to trajectory planning | CVPR 2024 | [Code](https://github.com/BraveGroup/Drive-WM) |
| **Panacea** | [Panacea: Panoramic and Controllable Video Generation for Autonomous Driving](https://arxiv.org/abs/2311.16813) | Controllable temporally and cross-view consistent panoramic generation | CVPR 2024 | [Code](https://github.com/wenyuqing/panacea) · [Project](https://panacea-ad.github.io/) |
| **OccWorld** | [OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving](https://arxiv.org/abs/2311.16038) | Joint future 3D occupancy and ego-motion prediction | ECCV 2024 | [Code](https://github.com/wzzheng/OccWorld) |
| **Copilot4D** | [Copilot4D: Learning Unsupervised World Models for Autonomous Driving via Discrete Diffusion](https://arxiv.org/abs/2311.01017) | Tokenized sensor world modeling with discrete diffusion | ICLR 2024 | — |
| **DriveDreamer** | [DriveDreamer: Towards Real-world-driven World Models for Autonomous Driving](https://arxiv.org/abs/2309.09777) | Real-world diffusion world model with structured traffic control | ECCV 2024 | [Code](https://github.com/JeffWang987/DriveDreamer) · [Project](https://drivedreamer.github.io/) |
| **ADriver-I** | [ADriver-I: A General World Model for Autonomous Driving](https://arxiv.org/abs/2311.13549) | Interleaved vision-action modeling with MLLM and diffusion | arXiv 2023 | — |
| **GAIA-1** | [GAIA-1: A Generative World Model for Autonomous Driving](https://arxiv.org/abs/2309.17080) | Autoregressive video, text, and action token world modeling | arXiv 2023 | [Blog](https://wayve.ai/thinking/scaling-gaia-1/) |

---

## Latent & Planning-Oriented World Models

Models that learn future representations or use predicted consequences for planning, trajectory evaluation, policy learning, or reinforcement learning. JEPA methods appear in the dedicated section below.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **DPR** | [Directional Pullback Regularization for Long-Horizon Rollout of Latent World Models in Autonomous Driving](https://arxiv.org/abs/2610.16139) | Kinematics-aware latent regularization improves physical consistency of long-horizon rollouts | arXiv 2026 | — |
| **RoXDrive** | [RoXDrive: Closed-Loop Reinforcement Learning for End-to-End Autonomous Driving via Action-Faithful Rollouts](https://arxiv.org/abs/2609.36851) | Closed-loop RL retains world-model rollouts that faithfully follow conditioning actions | arXiv 2026 | [Repository](https://github.com/Hongbin98/RoXDrive) · [Project](https://hongbin98.github.io/RoXDrive/) |
| **MomWorld** | [MomWorld: Momentum-Aware Latent World Model for Long-Horizon Autonomous Driving](https://arxiv.org/abs/2609.33737) | Latent momentum propagation and adaptive resets stabilize long-horizon planning | arXiv 2026 | — |
| **ReDrive** | [ReDrive: Shaping Representations with World Modeling for End-to-End Driving](https://arxiv.org/abs/2609.33854) | Future representation prediction strengthens planning features without inference-time world rollout | arXiv 2026 | — |
| **Relationally Grounded LWM** | [Relationally Grounded Latent World Models for Autonomous Driving](https://arxiv.org/abs/2609.24626) | Privileged traffic-graph semantics supervise latent states without extra inference branches | IROS RoBoWoMo Workshop 2026 | — |
| **GraphWorld** | [GraphWorld: Long-Horizon Planning with World Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2606.16274) | Interaction-graph latent world states for long-horizon planning | arXiv 2026 | — |
| **DeepSight** | [DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving](https://arxiv.org/abs/2605.10564) | Parallel long-horizon BEV latent-state prediction | [ICML 2026](https://proceedings.mlr.press/v306/zhang26gq.html) | [Code](https://github.com/hotdogcheesewhite/DeepSight) |
| **DriveFuture** | [DriveFuture: Future-Aware Latent World Models for Autonomous Driving](https://arxiv.org/abs/2605.09701) | Future-aware latent conditioning for diffusion trajectory planning | arXiv 2026 | — |
| **WorldDrive** | [Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948) | A shared vision-motion representation transfers trajectory-conditioned world learning to planning | [NeurIPS 2026 (accepted)](https://github.com/TabGuigui/WorldDrive) | [Code](https://github.com/TabGuigui/WorldDrive) |
| **DriveLaW** | [DriveLaW: Unifying Planning and Video Generation in a Latent Driving World](https://arxiv.org/abs/2512.23421) | Video-world latents are directly injected into a diffusion planner | CVPR 2026 | [Code](https://github.com/xiaomi-research/drivelaw) |
| **World4Drive** | [World4Drive: End-to-End Autonomous Driving via Intention-aware Physical Latent World Model](https://arxiv.org/abs/2507.00603) | Intention-aware latent futures for trajectory generation and selection | ICCV 2025 | [Code](https://github.com/ucaszyp/World4Drive) |
| **Raw2Drive** | [Raw2Drive: Reinforcement Learning with Aligned World Models for End-to-End Autonomous Driving (in CARLA v2)](https://arxiv.org/abs/2505.16394) | Aligns privileged and raw-sensor world models for model-based RL | NeurIPS 2025 | [Repository](https://github.com/Thinklab-SJTU/Raw2Drive) |
| **WoTE** | [End-to-End Driving with Online Trajectory Evaluation via BEV World Model](https://arxiv.org/abs/2504.01941) | BEV future states support online evaluation and selection of candidate trajectories | [ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Li_End-to-End_Driving_with_Online_Trajectory_Evaluation_via_BEV_World_Model_ICCV_2025_paper.html) | [Code](https://github.com/liyingyanUCAS/WoTE) |
| **LAW** | [Enhancing End-to-End Autonomous Driving with Latent World Model](https://arxiv.org/abs/2406.08481) | Ego-trajectory-conditioned future features provide self-supervised planning representations | [ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/6aa4967920e495e90aeeaa3acf18d019-Abstract-Conference.html) | [Code](https://github.com/BraveGroup/LAW) |
| **DriveWorld** | [DriveWorld: 4D Pre-trained Scene Understanding via World Models for Autonomous Driving](https://arxiv.org/abs/2405.04390) | Spatiotemporal latent dynamics for multi-task 4D pre-training | [CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/html/Min_DriveWorld_4D_Pre-trained_Scene_Understanding_via_World_Models_for_Autonomous_CVPR_2024_paper.html) | — |
| **Think2Drive** | [Think2Drive: Efficient Reinforcement Learning by Thinking in Latent World Model for Quasi-Realistic Autonomous Driving (in CARLA-v2)](https://arxiv.org/abs/2402.16720) | Latent imagination for model-based reinforcement learning | [ECCV 2024](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6129_ECCV_2024_paper.php) | — |
| **ViDAR** | [Visual Point Cloud Forecasting enables Scalable Autonomous Driving](https://arxiv.org/abs/2312.17655) | Future point-cloud forecasting as self-supervised driving pre-training | CVPR 2024 | [Code](https://github.com/OpenDriveLab/ViDAR) |
| **UniWorld** | [UniWorld: Autonomous Driving Pre-training via World Models](https://arxiv.org/abs/2308.07234) | Label-free 4D occupancy prediction for transferable driving pre-training | arXiv 2023 | — |
| **TrafficBots** | [TrafficBots: Towards World Models for Autonomous Driving Simulation and Motion Prediction](https://arxiv.org/abs/2303.04116) | Multi-agent world model for configurable traffic simulation and prediction | ICRA 2023 | [Code](https://github.com/zhejz/TrafficBots) |
| **MILE** | [Model-Based Imitation Learning for Urban Driving](https://proceedings.neurips.cc/paper_files/paper/2022/hash/827cb489449ea216e4a257c47e407d18-Abstract-Conference.html) | Joint latent world model and policy learned from offline driving video | NeurIPS 2022 | [Code](https://github.com/wayveai/mile) |

---

## World-Action & Action-Aligned Models

Models that couple future-world prediction with actions through joint generation, action-conditioned feedback, alignment, or verification. JEPA-based world-action models appear in the JEPA section.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **OccWAM** | [OccWAM: Occupancy World-Action Models with Joint Scene-to-Ego Flow Matching](https://arxiv.org/abs/2610.17688) | Joint occupancy and ego-trajectory flow matching refines scene-centric and ego-centric futures | arXiv 2026 | — |
| **SimVTA** | [SimVTA: Simulation-Grounded Video-Trajectory Alignment for Driving World Action Models](https://arxiv.org/abs/2610.13781) | Simulator-rendered candidate futures align video supervision with reward-optimized trajectories | arXiv 2026 | [Repository](https://github.com/OpenDriveLab/SimVTA) (code pending) · [Project](https://opendrivelab.com/SimVTA/) |
| **PlanWAM** | [PlanWAM: Planning-Shaped Future Representations for End-to-End Autonomous Driving](https://arxiv.org/abs/2610.11382) | A privileged future posterior teaches a history-only prior to predict planning-shaped futures | arXiv 2026 | [Repository](https://github.com/jinchan9/PlanWAM) (code pending) |
| **AffordDrive3D** | [AffordDrive3D: Affordance-Aware World-Action Modeling with Spatial Understanding](https://arxiv.org/abs/2610.11060) | Joint future geometry and drivable or collision-critical affordances guide action planning | arXiv 2026 | [Project](https://afforddrive3d.github.io/) |
| **ReWAM** | [ReWAM: Reciprocal World Action Models for Interactive Autonomous Driving](https://arxiv.org/abs/2609.39245) | Level-k reciprocal-response modeling couples ego and other-agent decisions | arXiv 2026 | — |
| **V2X-WAM** | [V2X-WAM: A Cooperative World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.37098) | Vehicle-infrastructure observations support action-conditioned occupancy and flow feedback | arXiv 2026 | — |
| **PhysWAM** | [PhysWAM: Physically Consistent World Action Model for Autonomous Driving](https://arxiv.org/abs/2609.37970) | Co-generates multiview video, metric depth, and ego motion under a shared 3D projection constraint | arXiv 2026 | — |
| **WALT** | [WALT: Learning World-Model-Aligned Latent Trajectories for Autonomous Driving](https://arxiv.org/abs/2609.30436) | Transfers world-model semantics into compact trajectory latents | arXiv 2026 | — |
| **DriveReferee** | [DriveReferee: Geometric Safety Verdicts Need Not Be Learned for Driving World-Action Models](https://arxiv.org/abs/2609.22762) | A learned geometry readout supports analytic collision and drivable-area checks | arXiv 2026 | — |
| **MM-Future** | [MM-Future: Multi-Mode Joint World-Action Modeling for Autonomous Driving](https://arxiv.org/abs/2609.20377) | Multiple paired scene-action futures with joint diffusion modeling | arXiv 2026 | — |
| **GeoWAM** | [GeoWAM: Visual Geometry World Action Models for Autonomous Driving](https://arxiv.org/abs/2608.23486) | Predicts future scene geometry and conditions ego actions on geometric dynamics | arXiv 2026 | — |
| **DA-WAM** | [DA-WAM: Decision-Aligned Future Latents for Driving World Models](https://arxiv.org/abs/2608.19085) | Action-conditioned future latents optimized for trajectory scoring | arXiv 2026 | — |
| **SimWAM** | [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468) | Uses future-video prediction as training-only supervision for an efficient action expert | arXiv 2026 | [Code](https://github.com/H-EmbodVis/SimWAM) |
| **DriveWAM** | [DriveWAM: Video Generative Priors Enable Scalable World-Action Modeling for Autonomous Driving](https://arxiv.org/abs/2605.28544) | Adapts a video diffusion transformer into an autoregressive video-action policy | arXiv 2026 | [Code](https://github.com/chenshi3/DriveWAM) · [Project](https://chenshi3.github.io/drivewam.github.io/) |
| **Latent-WAM** | [Latent-WAM: Latent World Action Modeling for End-to-End Autonomous Driving](https://arxiv.org/abs/2603.24581) | Compact spatial world tokens + causal latent dynamics for action planning | arXiv 2026 | — |
| **DrivingGPT** | [DrivingGPT: Unifying Driving World Modeling and Planning with Multi-modal Autoregressive Transformers](https://arxiv.org/abs/2412.18607) | Interleaved image and action tokens unify world simulation and planning by next-token prediction | [ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_DrivingGPT_Unifying_Driving_World_Modeling_and_Planning_with_Multi-modal_Autoregressive_ICCV_2025_paper.html) | — |

---

# JEPA for Autonomous Driving

Driving-related joint-embedding predictive methods are collected in one place, spanning representation pre-training, compact predictive states, planning, candidate scoring, and world-action modeling.

| Model | Paper | Driving Role | Venue | Resources |
| --- | --- | --- | --- | --- |
| **MORE** | [MORE: Learning Motion-Oriented Registers for Driving World Models and Planning](https://arxiv.org/abs/2610.14871) | Motion-conditioned V-JEPA registers form a compact shared interface for future prediction and planning | arXiv 2026 | — |
| **World4Scorer** | [World4Scorer: Outcome-Grounded World Modeling for Autonomous Driving](https://arxiv.org/abs/2609.36438) | Trajectory-conditioned JEPA states learn candidate scores from simulator outcomes and logged futures | arXiv 2026 | [Code](https://github.com/World4Scorer/World4Scorer) · [Project](https://world4scorer.github.io/) |
| **AD-E2E-JEPA** | [AD-E2E-JEPA: A Joint-Embedding Predictive Architecture For End-to-End Autonomous Driving](https://arxiv.org/abs/2609.34085) | Action-conditioned JEPA world model for efficient goal-conditioned zero-shot planning and downstream IL | arXiv 2026 | [Code](https://github.com/HaoranZhuExplorer/AD-E2E-JEPA) |
| **ForeDrive** | [ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model](https://arxiv.org/abs/2609.26299) | JEPA-style multi-horizon latent futures directly condition a DiT planner | arXiv 2026 | — |
| **WA-JEPA** | [WA-JEPA: Rethinking the Video JEPA Paradigm for World-Action Modeling in Autonomous Driving](https://arxiv.org/abs/2608.20974) | Future-masked V-JEPA + flow matching + joint future-scene / action prediction | arXiv 2026 | [Code](https://github.com/AFARI-Research/WA-JEPA) · [Project](https://wa-jepa.github.io/) |
| **Auto-JEPA** | [Auto-JEPA: A Latent World Model of Continuous Intent for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.29031) | Predicts planning-relevant continuous future-intent embeddings instead of dense future scenes | arXiv 2026 | [Code](https://github.com/NoctYang/Auto-JEPA) |
| **Drive-JEPA** | [Drive-JEPA: Video JEPA Meets Multimodal Trajectory Distillation for End-to-End Driving](https://arxiv.org/abs/2601.22032) | V-JEPA video pre-training aligned with proposal-based end-to-end planning | arXiv 2026 | [Code](https://github.com/linhanwang/Drive-JEPA) |
| **HanoiWorld** | [HanoiWorld: A Joint Embedding Predictive Architecture Based World Model for Autonomous Vehicle Controller](https://arxiv.org/abs/2601.01577) | JEPA-based recurrent world model for long-horizon autonomous-vehicle control | arXiv 2026 | — |
| **AD-L-JEPA** | [Self-Supervised Representation Learning with Joint Embedding Predictive Architecture for Automotive LiDAR Object Detection](https://arxiv.org/abs/2501.04969) | BEV LiDAR representation pre-training for downstream 3D detection | AAAI 2026 | [Code](https://github.com/HaoranZhuExplorer/adljepa) · [Project](https://ad-l-jepa.github.io/) |
| **LM-JEPA** | [Object Detection and Scene Perception for Connected and Autonomous Vehicles Using LM-JEPA](https://www.mdpi.com/1424-8220/26/15/4894) | Latent predictive representation learning for resource-efficient connected-vehicle perception | Sensors 2026 | — |

---

# Vision-Language-Action for Driving

The intersection of language-based reasoning, predictive world representations, and driving actions.

## World-Model-Enhanced VLA

VLA/VLM methods where future prediction or learned world representations directly contribute to reasoning or action generation.

| Model | Paper | World-Model / Reasoning Mechanism | Venue | Resources |
| --- | --- | --- | --- | --- |
| **SafeDriveVLA** | [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](https://arxiv.org/abs/2610.20609) | Navigation-conditioned latent dreaming identifies unsafe instruction following | CoRL 2026 (accepted) | [Code](https://github.com/ASGuard-UCI/safedrive-vla) · [Project](https://safedrive-vla.github.io/SafeDriveVLA/) |
| **DriveWLA** | [DriveWLA: Unifying Future Dynamics and Scene Semantics through World-Language-Action Modeling for Autonomous Driving](https://arxiv.org/abs/2610.17903) | World, language, and action experts share dynamics and semantic context; Flow-GRPO refines planning | arXiv 2026 | — |
| **VGGTWorld-VLA** | [VGGTWorld-VLA: Intent-Conditioned 3D World Evolution for Autonomous Driving](https://arxiv.org/abs/2610.11161) | Driving semantics and ego actions condition future 3D geometry in a VGGT-based world model | arXiv 2026 | — |
| **HyWorldVLA** | [HyWorldVLA: A Vision-Language-Action Model with Hybrid World Modeling for Autonomous Driving](https://arxiv.org/abs/2607.20988) | Combines pixel-level grounding with latent future prediction before action generation | arXiv 2026 | — |
| **WCog-VLA** | [WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.08375) | Semantic world cognition + generative joint multi-agent future modeling + Game-CoT | arXiv 2026 | — |
| **CoWorld-VLA** | [CoWorld-VLA: Thinking in a Multi-Expert World Model for Autonomous Driving](https://arxiv.org/abs/2605.10426) | Multi-expert world tokens for semantics, geometry, dynamics, and ego goals explicitly condition planning | arXiv 2026 | [Code](https://github.com/AFARI-Research/CoWorld-VLA) |
| **OneVL** | [Xiaomi OneVL: One-Step Latent Reasoning and Planning with Vision-Language Explanation](https://arxiv.org/abs/2604.18486) | Compact latent CoT is jointly supervised by language reasoning and a visual future-world decoder | arXiv 2026 | [Code](https://github.com/xiaomi-research/onevl) |
| **VLA-World** | [Learning Vision-Language-Action World Models for Autonomous Driving](https://arxiv.org/abs/2604.09059) | Generates an action-guided future image, then reasons over the imagined future to refine the trajectory | [CVPR Findings 2026](https://vlaworld.github.io/) | [Project](https://vlaworld.github.io/) |
| **ExploreVLA** | [ExploreVLA: Dense World Modeling and Exploration for End-to-End Autonomous Driving](https://arxiv.org/abs/2604.02714) | Uses world-model uncertainty as an intrinsic reward for safe exploration | ECCV 2026 | [Code](https://github.com/zihaosheng/ExploreVLA) |
| **Uni-World VLA** | [Uni-World VLA: Interleaved World Modeling and Planning for Autonomous Driving](https://arxiv.org/abs/2603.27287) | Alternates future-frame prediction and ego-action generation in one autoregressive sequence | arXiv 2026 | [Code](https://github.com/LogosRoboticsGroup/UniWorldVLA) |
| **DynVLA** | [DynVLA: Learning World Dynamics for Action Reasoning in Autonomous Driving](https://arxiv.org/abs/2603.11041) | Dynamics CoT compresses ego- and environment-centric future evolution into compact dynamics tokens | ICML 2026 | [Code](https://github.com/yaoyao-jpg/DynamicsVLA) · [Project](https://yaoyao-jpg.github.io/dynvla/) |
| **DriveWorld-VLA** | [DriveWorld-VLA: Unified Latent-Space World Modeling with Vision-Language-Action for Autonomous Driving](https://arxiv.org/abs/2602.06521) | Shared latent world states support action-conditioned imagination and VLA planning | [ICML 2026](https://proceedings.mlr.press/v306/jia26f.html) | [Code](https://github.com/liulin815/DriveWorld-VLA) |
| **DriveVLA-W0** | [DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving](https://arxiv.org/abs/2510.12796) | Future-image world modeling supplies dense self-supervision for VLA scaling | ICLR 2026 | [Code](https://github.com/BraveGroup/DriveVLA-W0) |
| **LWDrive** | [Layer-Wise World-Model-Guided Vision-Language Model Planning for Autonomous Driving](https://arxiv.org/abs/2606.29879) | Future-frame supervision shapes VLM hidden states for coarse-to-fine trajectory refinement | arXiv 2026 | [Repository](https://github.com/yachyc/LWDrive) |
| **DriveVLA-M0** | [Failure-Aware Memory Augmentation for Autonomous Driving](https://arxiv.org/abs/2608.10413) | Failure-aware latent memory with structurally grounded retrieval and lightweight test-time adaptation | ACM MM 2026 | [Code](https://github.com/ZebinX/DriveVLA-M0) |
| **FutureSightDrive** | [FutureSightDrive: Thinking Visually with Spatio-Temporal CoT for Autonomous Driving](https://arxiv.org/abs/2505.17685) | VLA first acts as a world model to generate a visual future CoT, then plans from it | NeurIPS 2025 | [Code](https://github.com/MIV-XJTU/FSDrive) · [Project](https://miv-xjtu.github.io/FSDrive.github.io/) |
| **OccLLaMA** | [OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving](https://arxiv.org/abs/2409.03272) | A shared occupancy-language-action vocabulary enables multimodal future prediction and planning | arXiv 2024 | [Project](https://vilonge.github.io/OccLLaMA_Page/) |

---

## Selected General Driving VLA

Selected architectural and data references for driving VLA. These papers are not necessarily world models themselves.

| Model | Paper | Main Focus | Venue | Resources |
| --- | --- | --- | --- | --- |
| **MindVLA-U1** | [MindVLA-U1: VLA Beats VA with Unified Streaming Architecture for Autonomous Driving](https://arxiv.org/abs/2605.12624) | Unified streaming language + continuous-action generation with memory | arXiv 2026 | [Project](https://mind-omni.github.io/projects/u1/index.html) |
| **OneDrive** | [OneDrive: Unified Multi-Paradigm Driving with Vision-Language-Action Models](https://arxiv.org/abs/2604.17915) | One causal VLM decoder for language, perception queries, and trajectory queries | arXiv 2026 | [Code](https://github.com/Z1zyw/OneDrive) |
| **UniDriveVLA** | [UniDriveVLA: Unifying Understanding, Perception, and Action Planning for Autonomous Driving](https://arxiv.org/abs/2604.02190) | Mixture-of-Transformers experts for semantic reasoning, spatial perception, and planning | arXiv 2026 | [Code](https://github.com/xiaomi-research/unidrivevla) |
| **OpenDriveVLA** | [OpenDriveVLA: Towards End-to-end Autonomous Driving with Large Vision Language Action Model](https://arxiv.org/abs/2503.23463) | 2D/3D vision-language alignment with agent–environment–ego interaction modeling | AAAI 2026 | [Code](https://github.com/DriveVLA/OpenDriveVLA) · [Project](https://drivevla.github.io/) |
| **Reasoning-VLA** | [Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving](https://arxiv.org/abs/2511.19912) | Parallel continuous action generation from reasoning-enhanced VLM features | arXiv 2025 | — |
| **AutoVLA** | [AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning](https://arxiv.org/abs/2506.13757) | Adaptive fast/slow CoT reasoning with physical action tokens and GRPO fine-tuning | NeurIPS 2025 | [Code](https://github.com/ucla-mobility/AutoVLA) · [Project](https://autovla.github.io/) |
| **Impromptu VLA** | [Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models](https://arxiv.org/abs/2505.23757) | Large open corner-case VLA dataset, benchmark, weights, and planning-oriented QA | NeurIPS 2025 | [Code](https://github.com/ahydchh/Impromptu-VLA) · [Project](https://ziming-liu.github.io/projects/impromptu-vla/index.html) |

---

# Benchmarks & Simulation

World-model fidelity benchmarks and planning evaluation platforms. Non-reactive evaluation and pseudo-simulation are distinguished from interactive closed-loop simulation; scores across these protocols are not interchangeable.

| Benchmark | Paper | Evaluation Focus | Venue | Resources |
| --- | --- | --- | --- | --- |
| **VehDyn** | [VehDyn: A Driving World Model Benchmark for Vehicle Dynamics](https://arxiv.org/abs/2609.33264) | Controlled CARLA-CarSim scenarios separate visual quality from kinematic and dynamic fidelity | arXiv 2026 | — |
| **WorldLens** | [WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World](https://arxiv.org/abs/2512.10958) | Evaluates generated worlds across visual, geometric, action, downstream-task, and human-preference criteria | [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Liang_WorldLens_Full-Spectrum_Evaluations_of_Driving_World_Models_in_Real_World_CVPR_2026_paper.pdf) | [Code](https://github.com/worldbench/WorldLens) · [Project](https://worldbench.github.io/worldlens) |
| **NAVSIM v2** | [Pseudo-Simulation for Autonomous Driving](https://arxiv.org/abs/2506.04218) | Pseudo-simulation uses perturbed future observations to evaluate recovery and planning robustness | CoRL 2025 | [Code](https://github.com/autonomousvision/navsim) |
| **HUGSIM** | [HUGSIM: A Real-Time, Photo-Realistic and Closed-Loop Simulator for Autonomous Driving](https://arxiv.org/abs/2412.01718) | 3D Gaussian reconstruction enables real-time photorealistic closed-loop policy evaluation | [IEEE TPAMI 2025](https://yiyiliao.github.io/) | [Code](https://github.com/hyzhou404/HUGSIM) · [Project](https://xdimlab.github.io/HUGSIM/) |
| **NAVSIM v1** | [NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking](https://arxiv.org/abs/2406.15349) | Non-reactive simulation-based metrics benchmark planning on real driving logs | NeurIPS Datasets and Benchmarks 2024 | [Code](https://github.com/autonomousvision/navsim/tree/v1.1) |
| **Bench2Drive** | [Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-To-End Autonomous Driving](https://arxiv.org/abs/2406.03877) | CARLA short-route closed-loop benchmark measures multiple driving abilities and failure modes | NeurIPS Datasets and Benchmarks 2024 | [Code](https://github.com/Thinklab-SJTU/Bench2Drive) · [Project](https://thinklab-sjtu.github.io/Bench2Drive/) |

---

# Related Work

Selected references outside the core driving taxonomy.

## Embodied / Robotics World Models

Selected embodied methods with direct relevance to joint world-action modeling.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **XPACE** | [XPACE: Joint World and Action Modeling from Heterogeneous Experience](https://arxiv.org/abs/2609.17372) | Shared video backbone jointly predicts robot actions and future video | arXiv 2026 | [Project](https://xpeng-robotics.github.io/xpace/) |

---

## General Video World Models

Selected non-driving references for controllable generation and shared-world consistency. Their evaluation domains are stated explicitly.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **WorldCast** | [WorldCast: Distributed Multiplayer World Models](https://arxiv.org/abs/2610.12412) | Distributed clients exchange player and scene states for consistent multiplayer worlds; evaluated in Counter-Strike 2 | arXiv 2026 | [Code](https://github.com/Ziyang-Ye/WorldCast) · [Project](https://ziyang-ye.github.io/WorldCast-Page/) |
| **Holo-World** | [Holo-World: Unified Camera, Object and Weather Control for Video World Model](https://arxiv.org/abs/2606.20083) | Unified camera, object, and weather control from a single source image | arXiv 2026 | [Repository](https://github.com/XiangchenYin/Holo-World) · [Project](https://xiangchenyin.github.io/Holo-World/) |

<!-- PAPERS_END -->

---

# Datasets & Toolkits

| Resource | Use in Driving World Models | Official Resources |
| --- | --- | --- |
| **nuScenes** | Multi-camera and LiDAR logs with scene annotations for forecasting, occupancy, and planning studies | [Dataset](https://www.nuscenes.org/nuscenes) · [Devkit](https://github.com/nutonomy/nuscenes-devkit) |
| **nuPlan** | Real driving logs, maps, and a closed-loop planning devkit; a data source for NAVSIM | [Dataset](https://www.nuscenes.org/nuplan) · [Devkit](https://github.com/motional/nuplan-devkit) |
| **OpenDV / OpenDV-YouTube** | Driving-video pre-training data and language annotations, with a smaller starter subset | [Data and Tools](https://github.com/OpenDriveLab/DriveAGI#opendv) |
| **OpenDWM** | Reusable training, inference, and evaluation implementation for driving-video world models | [Code and Checkpoints](https://github.com/SenseTime-FVG/OpenDWM) |

For planning evaluation, see [NAVSIM v1/v2, Bench2Drive, and HUGSIM](#benchmarks--simulation) above. Specify the dataset split, evaluator version, camera configuration, and scoring protocol when comparing results.

---

# Industrial World Models

Official research posts are listed separately from paper entries and are excluded from the paper-count badge.

| System | Official Technical Post | Focus | Year |
| --- | --- | --- | --- |
| **GAIA-3** | [Scaling World Models to Power Safety and Evaluation](https://wayve.ai/thinking/gaia-3/) | Generative simulation for repeatable driving-policy evaluation | 2025 |
| **Waymo World Model** | [A New Frontier for Autonomous Driving Simulation](https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation) | Camera/LiDAR simulation and controllable scenario generation | 2026 |

---

# Recent Updates

- **2026-10-19** — Expanded the public catalog from **71 to 112 papers**: added 40 verified references and restored one survey that previously existed only in YAML. Recent additions include **DriveWLA, OccWAM, MORE, SimVTA, PlanWAM, SafeDriveVLA, World4Scorer, CoDrive, PhysWAM**, and **RoXDrive**.
- **2026-10-19** — Added missing reference methods **Vista, LAW, WoTE, DrivingGPT, GAIA-2, MaskGWM, DOME, ReSim**, and **WorldDrive**, plus a dedicated benchmark section covering **WorldLens, VehDyn, NAVSIM v1/v2, Bench2Drive**, and **HUGSIM**.
- **2026-10-19** — Updated publication metadata and resource labels; removed the unavailable UniWorld repository link. Synchronized all paper entries with YAML and rebuilt the generator around the current JEPA/VLA taxonomy, with duplicate validation and a `--check` mode.
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

All paper tables and the paper-count / last-updated badges are generated from that file. Each paper belongs to exactly one primary category.

To add or update a paper:

1. Edit the corresponding entry in `data/papers.yaml`.
2. Regenerate the README:

```bash
pip install -r requirements.txt
python scripts/generate_readme.py
python scripts/generate_readme.py --check
```

3. Check the generated tables and links.
4. Open a pull request.

The generator replaces the paper-table block bounded by the inline markers `<!-- PAPERS_START -->` and `<!-- PAPERS_END -->`, and synchronizes the two metadata badges. Other sections can be edited manually.

### Suggested metadata for each paper

```yaml
schema_version: 2
updated_date: "2026-10-19"
papers:
  - model: ExampleModel
    title: Full paper title
    paper_url: https://arxiv.org/abs/2601.12345
    arxiv_id: "2601.12345"
    year: 2026
    venue: arXiv
    category: latent
    focus: One-line description of the predictive mechanism and its use
    publication_status: preprint
    published_date: "2026-01-18"
    code_url: ""
    project_url: ""
```

Optional `publication_url` links to an official publication or acceptance source. `publication_status` is `preprint`, `accepted`, or `published`. `published_date` records the first public posting; `verified_date` records the latest metadata check. Keep `year` aligned with the listed venue, even when the arXiv preprint appeared earlier.

For a repository link, `code_status` can be `released` (default), `partial`, `unreleased`, `repository-only`, or `data-only`. Mark a placeholder repository honestly; an announced code release is not the same as an available implementation. Additional resources such as a blog or reading list can be stored as `resources: [{label: Blog, url: https://example.com}]`.

Recommended `category` values:

```text
survey
generative
latent
world-action
jepa
vla-world
vla-general
benchmark
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

