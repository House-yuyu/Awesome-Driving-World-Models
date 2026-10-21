# Awesome World Models 🌍

<p align="center">
  <img src="https://img.shields.io/badge/papers-161-blue" alt="Papers">
  <img src="https://img.shields.io/badge/last%20updated-2026--10--21-brightgreen" alt="Last Updated">
  <img src="https://img.shields.io/badge/PRs-welcome-orange" alt="PRs Welcome">
</p>

A curated **cross-domain bibliography of world models** across **interactive environments and games, robotics and embodied AI, healthcare and biology, social/multi-agent systems, physics and weather, general video/spatial worlds, and autonomous driving**.

> **What happens next, and what changes after an action or intervention?**

## Scope

| Model type | Included role |
| --- | --- |
| **Predictive / actionable world models** | Predict future dynamics or the consequences of actions, decisions and interventions |
| **World foundation / predictive representation models** | Learn latent future representations for perception or planning |
| **Related simulators / evaluation tools** | Simulated interactions and benchmarks; not necessarily learned causal world models |

Papers have one primary category. Preprints are labeled arXiv; **Code**, **Repository**, **Project** and **Data** denote different resource status. Agent simulators and representation learning papers are not automatically considered validated causal world models.

## Contents

- [Surveys & Perspectives](#surveys--perspectives)
- [Foundations & General World Models](#foundations--general-world-models)
- [Interactive Worlds & Games](#interactive-worlds--games)
- [Robotics & Embodied World Models](#robotics--embodied-world-models)
- [Medical & Biological World Models](#medical--biological-world-models)
- [Social & Multi-Agent World Models](#social--multi-agent-world-models)
- [Physics, Weather & Scientific World Models](#physics-weather--scientific-world-models)
- [Video & Spatial World Models](#video--spatial-world-models)
- [General World-Model Benchmarks](#general-world-model-benchmarks)
- [Autonomous Driving World Models](#autonomous-driving-world-models)
  - [Generative driving worlds](#driving-generative--explicit-state-models)
  - [Latent driving prediction and planning](#driving-latent--planning-oriented-models)
  - [World-action driving models](#driving-world-action--action-aligned-models)
  - [Driving JEPA](#driving-jepa--predictive-representations)
  - [Driving world-aware VLA](#driving-world-model-enhanced-vla)
  - [Related driving VLA](#driving-selected-general-vla-context)
  - [Driving benchmarks](#driving-benchmarks--simulation)
- [Datasets & Toolkits](#datasets--toolkits)
- [Industrial & Research Systems](#industrial--research-systems)
- [Recent Updates](#recent-updates)
- [Definitions & Evaluation](#definitions--evaluation)
- [Contributing](#contributing)

---

<!-- PAPERS_START -->

# Surveys & Perspectives

Cross-domain world-model reviews.

| Work | Paper | Focus | Venue | Resources |
| --- | --- | --- | --- | --- |
| **Embodied WM Survey** | [World Models for Embodied Intelligence: From Plausible to Controllable to Actionable](https://arxiv.org/abs/2609.16697) | Capability hierarchy from plausible prediction to controllable and actionable embodied models | arXiv 2026 | — |
| **Latent WM Survey** | [Latent World Models for Automated Driving: A Unified Taxonomy, Evaluation Framework, and Open Challenges](https://arxiv.org/abs/2603.09086) | Latent-state taxonomy, evaluation, and deployment challenges | arXiv 2026 | — |
| **DWM Survey** | [The Role of World Models in Shaping Autonomous Driving: A Comprehensive Survey](https://arxiv.org/abs/2502.10498) | Driving world models by predicted scene modality | [Frontiers of Computer Science 2026 (accepted)](https://journal.hep.com.cn/fcs/EN/10.1007/s11704-026-60102-1) | [Paper List](https://github.com/LMD0311/Awesome-World-Model) |
| **AV JEPA Survey** | [Joint Embedding Predictive Architecture for Autonomous Vehicle Safety and Security: A Comprehensive Survey](https://www.sciencedirect.com/science/article/pii/S1474034626002909) | JEPA for autonomous-vehicle perception, safety, security, and deployment | Advanced Engineering Informatics 2026 | — |
| **Medical World Models Survey** | [Medical world models: representing medical states, modelling clinical dynamics and guiding intervention policies](https://arxiv.org/abs/2606.16721) | Patient dynamics and intervention planning | arXiv 2026 | [Repository](https://github.com/1999kevin/awesome_medical_world_models) |
| **Robotics World Model Survey** | [World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/abs/2605.00080) | Robot dynamics and policy learning | arXiv 2026 | — |
| **VLA4AD Survey** | [A Survey on Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2506.24044) | Driving VLA architectures, datasets, evaluation, and research trends | ICCV Workshops 2025 | [Paper List](https://github.com/JohnsonJiang1996/Awesome-VLA4AD) |
| **WMAD Survey** | [A Survey of World Models for Autonomous Driving](https://arxiv.org/abs/2501.11260) | Generation, planning, and prediction–planning interaction | arXiv 2025 | [Paper List](https://github.com/FengZicai/AwesomeWMAD) |
| **Embodied World Model Survey** | [A Comprehensive Survey on World Models for Embodied AI](https://arxiv.org/abs/2510.16732) | World-model taxonomy across embodied applications | arXiv 2025 | [Repository](https://github.com/Li-Zn-H/AwesomeWorldModels) |

---

# Foundations & General World Models

Latent dynamics and general predictive world representation learning.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **DreamerV3** | [Mastering Diverse Control Tasks Through World Models](https://www.nature.com/articles/s41586-025-08744-2) | General imagination-based model-based reinforcement learning | Nature 2025 | [Code](https://github.com/danijar/dreamerv3) |
| **V-JEPA 2** | [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) | Predictive video features and action-conditioned robot planning | arXiv 2025 | [Code](https://github.com/facebookresearch/vjepa2) |
| **TD-MPC2** | [TD-MPC2: Scalable, Robust World Models for Continuous Control](https://arxiv.org/abs/2310.16828) | Latent dynamics and trajectory optimization | ICLR 2024 | [Code](https://github.com/nicklashansen/tdmpc2) |
| **DreamerV2** | [Mastering Atari with Discrete World Models](https://arxiv.org/abs/2010.02193) | Discrete learned dynamics for Atari control | ICLR 2021 | [Code](https://github.com/danijar/dreamerv2) |
| **Dreamer** | [Dream to Control: Learning Behaviors by Latent Imagination](https://arxiv.org/abs/1912.01603) | Imagined latent trajectories train control policies | ICLR 2020 | [Code](https://github.com/danijar/dreamer) |
| **PlaNet** | [Learning Latent Dynamics for Planning from Pixels](https://arxiv.org/abs/1811.04551) | Pixel-to-latent dynamics for model-based planning | ICML 2019 | [Code](https://github.com/google-research/planet) |
| **World Models (Ha and Schmidhuber)** | [World Models](https://arxiv.org/abs/1803.10122) | Latent world dynamics for imagined agent policies | arXiv 2018 | — |

---

# Interactive Worlds & Games

Controllable generated interactive environments and playable simulations.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **GameNGen** | [Diffusion Models Are Real-Time Game Engines](https://arxiv.org/abs/2408.14837) | Action-conditioned diffusion game engine | ICLR 2025 | — |
| **GameFactory** | [GameFactory: Creating New Games with Generative Interactive Videos](https://arxiv.org/abs/2501.08325) | Action-controlled video games with scene generalization | ICCV 2025 | [Code](https://github.com/KlingAIResearch/GameFactory) (partial) |
| **Matrix-Game 2.0** | [Matrix-Game 2.0: An Open-Source, Real-Time, and Streaming Interactive World Model](https://arxiv.org/abs/2508.13009) | Real-time neural games steered by player actions | arXiv 2025 | [Code](https://github.com/SkyworkAI/Matrix-Game) |
| **Genie** | [Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391) | Learned latent actions for playable generated worlds | arXiv 2024 | — |
| **DIAMOND** | [Diffusion for World Modeling: Visual Details Matter in Atari](https://arxiv.org/abs/2405.12399) | Diffusion dynamics for Atari control and game rollouts | NeurIPS 2024 | [Code](https://github.com/eloialonso/diamond) |

---

# Robotics & Embodied World Models

Robot-action-conditioned video, imagined state and model-based policies.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **XPACE** | [XPACE: Joint World and Action Modeling from Heterogeneous Experience](https://arxiv.org/abs/2609.17372) | Shared video backbone jointly predicts robot actions and future video | arXiv 2026 | [Project](https://xpeng-robotics.github.io/xpace/) |
| **DreamDojo** | [DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](https://proceedings.mlr.press/v306/gao26q.html) | Action-conditioned robot dynamics learned from human video | ICML 2026 | [Code](https://github.com/NVIDIA/DreamDojo) |
| **DreamGen** | [DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories](https://arxiv.org/abs/2505.12705) | Synthetic world trajectories for robot policies | arXiv 2025 | — |
| **WorldVLA** | [WorldVLA: Towards Autoregressive Action World Model](https://arxiv.org/abs/2506.21539) | Shared autoregressive world and action model | arXiv 2025 | — |
| **SurgWorld** | [SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling](https://arxiv.org/abs/2512.23162) | Surgical world dynamics for robot imitation | arXiv 2025 | — |
| **RoboDreamer** | [RoboDreamer: Learning Compositional World Models for Robot Imagination](https://arxiv.org/abs/2404.12377) | Compositional robot world prediction | ICML 2024 | [Code](https://github.com/UMass-Embodied-AGI/robodreamer) |
| **IRASim** | [IRASim: Learning Interactive Real-Robot Action Simulators](https://arxiv.org/abs/2406.14540) | Action-conditioned robot video simulation | arXiv 2024 | [Code](https://github.com/bytedance/IRASim) |
| **GR-2** | [GR-2: A Generative Video-Language-Action Model with Web-Scale Knowledge for Robot Manipulation](https://arxiv.org/abs/2410.06158) | Joint robot action and future video modeling | arXiv 2024 | — |
| **UniPi** | [Learning Universal Policies via Text-Guided Video Generation](https://arxiv.org/abs/2302.00111) | Text-guided imagined plans translated into actions | NeurIPS 2023 | — |

---

# Medical & Biological World Models

Patient, disease, imaging and cell-state forecasting or simulation.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **MedDreamer** | [MedDreamer: Model-Based Reinforcement Learning with Latent Imagination on Complex EHRs for Clinical Decision Support](https://arxiv.org/abs/2505.19785) | Clinical decisions from imagined patient trajectories | KDD 2026 | [Code](https://github.com/xuqianyi/medDreamer) |
| **EHRWorld** | [EHRWorld: A Patient-Centric Medical World Model for Long-Horizon Clinical Trajectories](https://arxiv.org/abs/2602.03569) | Predicts longitudinal patient states and outcomes | arXiv 2026 | — |
| **Brain-WM** | [Brain-WM: Brain Glioblastoma World Model](https://arxiv.org/abs/2603.07562) | Brain tumor evolution and disease progression | arXiv 2026 | — |
| **EchoJEPA** | [EchoJEPA: A Latent Predictive Foundation Model for Echocardiography](https://arxiv.org/abs/2602.02603) | Ultrasound predictive features, not clinical intervention simulator | arXiv 2026 | [Code](https://github.com/bowang-lab/EchoJEPA) |
| **X-WIN** | [X-WIN: Building Chest Radiograph World Model via Predictive Sensing](https://arxiv.org/abs/2511.14918) | Predictive chest X-ray volumetric representations | CVPR 2026 | — |
| **HounsWorld** | [HounsWorld: A Multimodal World Model for Hidden Patient-State Readout, Reconstruction, and Simulation](https://arxiv.org/abs/2608.12904) | CT and clinical text hidden patient-state simulation | arXiv 2026 | — |
| **UltraWorld** | [UltraWorld: Learning Interactive Ultrasound World Models from Untracked Clinical Videos with Acoustic Sampling Map](https://arxiv.org/abs/2610.09785) | Interactive ultrasound image dynamics under probe actions | arXiv 2026 | — |
| **Lingshu-Cell** | [Lingshu-Cell: A Generative Cellular World Model for Transcriptome Modeling toward Virtual Cells](https://arxiv.org/abs/2603.25240) | Cellular transcriptome responses to interventions | arXiv 2026 | — |
| **MeWM** | [Medical World Model: Generative Simulation of Tumor Evolution for Treatment Planning](https://arxiv.org/abs/2506.02327) | Treatment-conditioned tumor simulation and clinical planning | ICCV 2025 | [Code](https://github.com/scott-yjyang/MeWM) |
| **CheXWorld** | [CheXWorld: Exploring Image World Modeling for Radiograph Representation Learning](https://arxiv.org/abs/2504.13820) | Predictive radiograph representations; related foundation model | CVPR 2025 | [Code](https://github.com/LeapLabTHU/CheXWorld) |
| **Brain-JEPA** | [Brain-JEPA: Brain Dynamics Foundation Model with Gradient Positioning and Spatiotemporal Masking](https://arxiv.org/abs/2409.19407) | Spatiotemporal fMRI predictive representation model | NeurIPS 2024 | [Code](https://github.com/Eric-LRL/Brain-JEPA) |

---

# Social & Multi-Agent World Models

Social-state transitions and related agent simulation systems.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **Social World Models** | [Social World Models](https://arxiv.org/abs/2509.00559) | Predicts interpersonal actions and hidden social states | arXiv 2025 | — |
| **SOTOPIA** | [SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/hash/b3075b88e583a0e98d8b24338a613060-Abstract-Conference.html) | Interactive agent social evaluation environment | ICLR 2024 | [Code](https://github.com/sotopia-lab/sotopia) |
| **OASIS** | [OASIS: Open Agent Social Interaction Simulations with One Million Agents](https://arxiv.org/abs/2411.11581) | Evolving social-network multi-agent simulations | arXiv 2024 | — |
| **Generative Agents** | [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) | Memory-based multi-agent social simulator | UIST 2023 | [Code](https://github.com/joonspk-research/generative_agents) |
| **Concordia** | [Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia](https://arxiv.org/abs/2312.03664) | Environment-grounded generative social agents | arXiv 2023 | [Code](https://github.com/google-deepmind/concordia) |

---

# Physics, Weather & Scientific World Models

Learned physical and geophysical dynamical systems.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **NeuralGCM** | [Neural general circulation models for weather and climate](https://www.nature.com/articles/s41586-024-07744-y) | Differentiable climate and atmosphere dynamic simulation | Nature 2024 | [Code](https://github.com/google-research/neuralgcm) |
| **GenCast** | [Probabilistic weather forecasting with machine learning](https://www.nature.com/articles/s41586-024-08252-9) | Probabilistic atmospheric forecasts | Nature 2024 | — |
| **GraphCast** | [Learning skillful medium-range global weather forecasting](https://www.science.org/doi/10.1126/science.adi2336) | Graph neural forecasting of weather dynamics | Science 2023 | [Code](https://github.com/google-deepmind/graphcast) |
| **FourCastNet** | [FourCastNet: A Global Data-driven High-resolution Weather Model using Adaptive Fourier Neural Operators](https://arxiv.org/abs/2202.11214) | Global atmospheric forecasting with Fourier operators | arXiv 2022 | [Code](https://github.com/NVlabs/FourCastNet) |
| **MeshGraphNets** | [Learning Mesh-Based Simulation with Graph Networks](https://arxiv.org/abs/2010.03409) | Fluid and mesh state transitions | ICLR 2021 | — |
| **Graph Physics Simulator** | [Learning to Simulate Complex Physics with Graph Networks](https://arxiv.org/abs/2002.09405) | Graph-based dynamics for interacting particles | ICML 2020 | — |

---

# Video & Spatial World Models

Predictive and controllable representations of visual worlds.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **WorldCast** | [WorldCast: Distributed Multiplayer World Models](https://arxiv.org/abs/2610.12412) | Distributed clients exchange player and scene states for consistent multiplayer worlds; evaluated in Counter-Strike 2 | arXiv 2026 | [Code](https://github.com/Ziyang-Ye/WorldCast) · [Project](https://ziyang-ye.github.io/WorldCast-Page/) |
| **Holo-World** | [Holo-World: Unified Camera, Object and Weather Control for Video World Model](https://arxiv.org/abs/2606.20083) | Unified camera, object, and weather control from a single source image | arXiv 2026 | [Repository](https://github.com/XiangchenYin/Holo-World) · [Project](https://xiangchenyin.github.io/Holo-World/) |
| **V-JEPA** | [Revisiting Feature Prediction for Learning Visual Representations from Video](https://arxiv.org/abs/2404.08471) | Predictive visual representations related to world modeling | arXiv 2024 | — |

---

# General World-Model Benchmarks

Evaluation across action fidelity, physical consistency and geometry.

| Benchmark | Paper | Evaluation Focus | Venue | Resources |
| --- | --- | --- | --- | --- |
| **4DWorldBench** | [4DWorldBench: A Comprehensive Evaluation Framework for 3D/4D World Generation Models](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_4DWorldBench_A_Comprehensive_Evaluation_Framework_for_3D4D_World_Generation_Models_CVPR_2026_paper.html) | Evaluates geometric and temporal world generation | CVPR 2026 | — |
| **WorldSimBench** | [WorldSimBench: Towards Video Generation Models as World Simulators](https://proceedings.mlr.press/v267/qin25f.html) | Evaluates interactive fidelity of generative world simulators | ICML 2025 | — |
| **PhysBench** | [PhysBench: Benchmarking and Enhancing Vision-Language Models for Physical World Understanding](https://arxiv.org/abs/2501.16411) | Tests physical understanding, related benchmark | ICLR 2025 | — |

---

# Autonomous Driving World Models

Autonomous driving is one application of world models, including generation, latent prediction, world-action, JEPA, VLA and benchmarks.

## Driving: Generative & Explicit-State Models

RGB, LiDAR, occupancy and future-geometry driving worlds.

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

## Driving: Latent & Planning-Oriented Models

Future latent states and world-model-based driving plans.

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

## Driving: World-Action & Action-Aligned Models

Driving models that couple predictive states to actions.

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

## Driving: JEPA & Predictive Representations

Driving predictive representation and joint-embedding methods.

| Model | Paper | Key Idea | Venue | Resources |
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

## Driving: World-Model-Enhanced VLA

Driving VLA using future world states or features.

| Model | Paper | Key Idea | Venue | Resources |
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

## Driving: Selected General VLA (Context)

Related driving VLA references, not necessarily world models.

| Model | Paper | Key Idea | Venue | Resources |
| --- | --- | --- | --- | --- |
| **MindVLA-U1** | [MindVLA-U1: VLA Beats VA with Unified Streaming Architecture for Autonomous Driving](https://arxiv.org/abs/2605.12624) | Unified streaming language + continuous-action generation with memory | arXiv 2026 | [Project](https://mind-omni.github.io/projects/u1/index.html) |
| **OneDrive** | [OneDrive: Unified Multi-Paradigm Driving with Vision-Language-Action Models](https://arxiv.org/abs/2604.17915) | One causal VLM decoder for language, perception queries, and trajectory queries | arXiv 2026 | [Code](https://github.com/Z1zyw/OneDrive) |
| **UniDriveVLA** | [UniDriveVLA: Unifying Understanding, Perception, and Action Planning for Autonomous Driving](https://arxiv.org/abs/2604.02190) | Mixture-of-Transformers experts for semantic reasoning, spatial perception, and planning | arXiv 2026 | [Code](https://github.com/xiaomi-research/unidrivevla) |
| **OpenDriveVLA** | [OpenDriveVLA: Towards End-to-end Autonomous Driving with Large Vision Language Action Model](https://arxiv.org/abs/2503.23463) | 2D/3D vision-language alignment with agent–environment–ego interaction modeling | AAAI 2026 | [Code](https://github.com/DriveVLA/OpenDriveVLA) · [Project](https://drivevla.github.io/) |
| **Reasoning-VLA** | [Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving](https://arxiv.org/abs/2511.19912) | Parallel continuous action generation from reasoning-enhanced VLM features | arXiv 2025 | — |
| **AutoVLA** | [AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning](https://arxiv.org/abs/2506.13757) | Adaptive fast/slow CoT reasoning with physical action tokens and GRPO fine-tuning | NeurIPS 2025 | [Code](https://github.com/ucla-mobility/AutoVLA) · [Project](https://autovla.github.io/) |
| **Impromptu VLA** | [Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models](https://arxiv.org/abs/2505.23757) | Large open corner-case VLA dataset, benchmark, weights, and planning-oriented QA | NeurIPS 2025 | [Code](https://github.com/ahydchh/Impromptu-VLA) · [Project](https://ziming-liu.github.io/projects/impromptu-vla/index.html) |

---

## Driving: Benchmarks & Simulation

Driving simulation and evaluation protocols.

| Benchmark | Paper | Evaluation Focus | Venue | Resources |
| --- | --- | --- | --- | --- |
| **VehDyn** | [VehDyn: A Driving World Model Benchmark for Vehicle Dynamics](https://arxiv.org/abs/2609.33264) | Controlled CARLA-CarSim scenarios separate visual quality from kinematic and dynamic fidelity | arXiv 2026 | — |
| **WorldLens** | [WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World](https://arxiv.org/abs/2512.10958) | Evaluates generated worlds across visual, geometric, action, downstream-task, and human-preference criteria | [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Liang_WorldLens_Full-Spectrum_Evaluations_of_Driving_World_Models_in_Real_World_CVPR_2026_paper.pdf) | [Code](https://github.com/worldbench/WorldLens) · [Project](https://worldbench.github.io/worldlens) |
| **NAVSIM v2** | [Pseudo-Simulation for Autonomous Driving](https://arxiv.org/abs/2506.04218) | Pseudo-simulation uses perturbed future observations to evaluate recovery and planning robustness | CoRL 2025 | [Code](https://github.com/autonomousvision/navsim) |
| **HUGSIM** | [HUGSIM: A Real-Time, Photo-Realistic and Closed-Loop Simulator for Autonomous Driving](https://arxiv.org/abs/2412.01718) | 3D Gaussian reconstruction enables real-time photorealistic closed-loop policy evaluation | [IEEE TPAMI 2025](https://yiyiliao.github.io/) | [Code](https://github.com/hyzhou404/HUGSIM) · [Project](https://xdimlab.github.io/HUGSIM/) |
| **NAVSIM v1** | [NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking](https://arxiv.org/abs/2406.15349) | Non-reactive simulation-based metrics benchmark planning on real driving logs | NeurIPS Datasets and Benchmarks 2024 | [Code](https://github.com/autonomousvision/navsim/tree/v1.1) |
| **Bench2Drive** | [Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-To-End Autonomous Driving](https://arxiv.org/abs/2406.03877) | CARLA short-route closed-loop benchmark measures multiple driving abilities and failure modes | NeurIPS Datasets and Benchmarks 2024 | [Code](https://github.com/Thinklab-SJTU/Bench2Drive) · [Project](https://thinklab-sjtu.github.io/Bench2Drive/) |

<!-- PAPERS_END -->

# Datasets & Toolkits

| Domain | Resource | Purpose | Link |
| --- | --- | --- | --- |
| General control | DeepMind Control Suite | Model-based reinforcement learning | [Code](https://github.com/google-deepmind/dm_control) |
| Robotics | Open X-Embodiment | Multi-robot action demonstrations | [Data](https://github.com/google-deepmind/open_x_embodiment) |
| Robotics | DROID | Robot manipulation trajectories | [Data](https://github.com/droid-dataset/droid) |
| Games | Arcade Learning Environment | Atari rollout and planning | [Code](https://github.com/Farama-Foundation/Arcade-Learning-Environment) |
| Medicine | MIMIC-IV | Patient trajectories (credentialed access) | [PhysioNet](https://physionet.org/content/mimiciv/) |
| Medicine | HCC-TACE-Seg | Tumor progression and treatment context | [TCIA](https://www.cancerimagingarchive.net/collection/hcc-tace-seg/) |
| Weather | ERA5 | Climate/weather trajectories | [Copernicus](https://cds.climate.copernicus.eu/) |
| Weather | WeatherBench 2 | Forecast evaluation | [Code](https://github.com/google-research/weatherbench2) |
| Driving | nuScenes / nuPlan | Multimodal trajectories and planning | [nuScenes](https://www.nuscenes.org/nuscenes) · [nuPlan](https://www.nuscenes.org/nuplan) |
| Driving | NAVSIM / Bench2Drive | Planning evaluation and closed-loop tests | [NAVSIM](https://github.com/autonomousvision/navsim) · [Bench2Drive](https://github.com/Thinklab-SJTU/Bench2Drive) |

# Industrial & Research Systems

Official project/industry releases here are not counted as scholarly publications.

| System | Domain | Link |
| --- | --- | --- |
| Genie 2 | Interactive environments | [DeepMind](https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/) |
| Genie 3 | Interactive environments | [DeepMind](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) |
| Marble | Spatial worlds | [World Labs](https://www.worldlabs.ai/blog/marble-world-model) |
| Matrix-Game 4 | Interactive games | [Repository](https://github.com/SkyworkAI/Matrix-Game/tree/main/Matrix-Game-4) |
| NVIDIA Cosmos | Physical AI | [Repository](https://github.com/NVIDIA/cosmos) |
| GAIA-3 | Driving | [Wayve](https://wayve.ai/thinking/gaia-3/) |
| Waymo World Model | Driving | [Waymo](https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation) |

# Recent Updates

- **2026-10-21:** Reorganized the collection around all-scenario world models and expanded it to medicine, robotics, interactive games, social simulation, science and general model evaluation.
- **2026-10-21:** Updated the metadata and README generator together, preserving the original driving literature within one application.
- **2026-10-19:** Previously expanded autonomous-driving JEPA, VLA, latent prediction and benchmarks.

# Definitions & Evaluation

**Latent models** predict learned future states. **Generative world models** output predicted video, geometry, medical images, or physical fields. **Action-conditioned models** approximate state changes caused by an agent or intervention. **Interactive world models** support repeated action–state feedback. Predictive video SSL is an enabling technology, but not automatically a complete environment simulator.

Evaluate temporal consistency, physical and action fidelity, long-horizon reliability, meaningful counterfactuals, and downstream policy value. Medical use requires independent clinical validation; social simulations are not established descriptions of real people's behavior.

# Contributing

The source of truth is `data/papers.yaml`. Paper tables and badges are generated by `scripts/generate_readme.py`. Edits inside the paper block will be overwritten during regeneration.

```bash
pip install -r requirements.txt
python scripts/generate_readme.py
python scripts/generate_readme.py --check
```

Valid categories: `survey`, `foundations`, `interactive`, `robotics`, `medical`, `social`, `physics`, `video-spatial`, `bench-general`, and driving-specific `generative`, `latent`, `world-action`, `jepa`, `vla-world`, `vla-general`, `benchmark`.

Supply a paper, publication status, specific predictive mechanism and verified code links. Code states include `released`, `partial`, `repository-only`, `unreleased` and `data-only`.

# Repository Structure

```text
.
├── README.md
├── data/papers.yaml
├── scripts/generate_readme.py
└── requirements.txt
```

# Acknowledgements

Preserving the original autonomous-driving bibliography, this project expands to a broader research landscape spanning dynamic environments, interactive agents and scientific predictions.
