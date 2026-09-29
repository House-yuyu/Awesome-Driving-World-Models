# Awesome Autonomous Driving World Models

A curated list of research papers on world models for autonomous driving, including generative world models, latent predictive models, world-action models, and JEPA-based representation learning.

This list focuses on world-model-related research in the driving domain. Papers from related fields (robotics, video generation) are included as background reference where relevant.

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

- **World Models for Embodied Intelligence: From Plausible to Controllable to Actionable** — *arXiv, 2026*
  [Paper](https://arxiv.org/abs/2609.16697)
  `Survey` `World Model` `Embodied Intelligence` `Review`
  A comprehensive survey that introduces a three-level capability framework (Plausible, Controllable, Actionable) for world models in embodied intelligence, covering manipulation, navigation, locomotion, and autonomous driving.

## Driving World Models

### Generative World Models

- **HelloWorld: Towards Practical Applications of Generative Driving World Models** — *arXiv, 2026*
  [Paper](https://arxiv.org/abs/2609.28931) [Project](https://helloworld-4d.github.io)
  `Generative World Model` `Simulation` `Counterfactual` `Multi-sensor` `Diffusion`
  HelloWorld is a 2B-parameter generative driving world model system that supports synchronized seven-camera RGB generation and conditional LiDAR synthesis for scalable data generation and interactive simulation.

### Latent / Predictive World Models

- **Auto-JEPA: A Latent World Model of Continuous Intent for End-to-End Autonomous Driving** — *arXiv, 2026*
  [Code](https://github.com/NoctYang/Auto-JEPA)
  `JEPA` `Latent World Model` `Intent Prediction` `Planning` `Action-conditioned`
  Auto-JEPA is an action-oriented latent world model that learns continuous future driving intent through joint-embedding prediction, retrieving executable trajectories from a fixed trajectory memory.

- **Drive-JEPA: Video JEPA Meets Multimodal Trajectory Distillation for End-to-End Driving** — *arXiv, 2026*
  [Paper](https://arxiv.org/abs/2601.22032) [Code](https://github.com/linhanwang/Drive-JEPA)
  `V-JEPA` `Video Prediction` `Trajectory Distillation` `Planning` `End-to-End Driving`
  Drive-JEPA integrates Video JEPA with multimodal trajectory distillation, pretraining a ViT encoder on driving videos and distilling diverse simulator-generated trajectories for end-to-end driving.

- **ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model** — *arXiv, 2026*
  `Latent World Model` `Planning` `Diffusion Transformer` `JEPA-style` `End-to-End Driving`
  ForeDrive learns a planning-relevant latent representation and couples it asymmetrically to a DiT planner, using multi-horizon future latents as guidance for trajectory generation.

- **WALT: Learning World-Model-Aligned Latent Trajectories for Autonomous Driving** — *arXiv, 2026*
  [Paper](https://arxiv.org/abs/2609.30436)
  `World Model Alignment` `Latent Trajectory` `REPA` `JEPA` `Planning`
  WALT learns a compact generative trajectory latent space by transferring semantic knowledge from a frozen pretrained driving world model, addressing the mismatch between visual world states and geometric trajectories.

### World-Action Models

- **MM-Future: Multi-Mode Joint World-Action Modeling for Autonomous Driving** — *arXiv, 2026*
  `World-Action Model` `Multi-mode` `Diffusion Transformer` `Planning` `BEV` `Action-conditioned`
  MM-Future is a world-action model that generates multiple paired scene-action hypotheses and models bidirectional interaction within each pair for autonomous driving.

- **WA-JEPA: Rethinking the Video JEPA Paradigm for World-Action Modeling in Autonomous Driving** — *arXiv, 2026*
  [Code](https://github.com/AFARI-Research/WA-JEPA)
  `WA-JEPA` `V-JEPA` `World-Action Model` `Flow Matching` `Planning` `Action-conditioned`
  WA-JEPA rethinks the V-JEPA paradigm for world-action modeling in autonomous driving, using hybrid future-masked pre-training and conditional flow matching over latent futures.

## Representation Learning

### JEPA-based Methods

- **Self-Supervised Representation Learning with Joint Embedding Predictive Architecture for Automotive LiDAR Object Detection (AD-L-JEPA)** — *arXiv, 2025*
  [Paper](https://arxiv.org/abs/2501.4969)
  `JEPA` `LiDAR` `Self-supervised Learning` `BEV` `Object Detection` `Pre-training`
  AD-L-JEPA is the first JEPA-based self-supervised pre-training framework for automotive LiDAR object detection, predicting BEV embeddings instead of reconstructing masked point clouds.

## Related Work

### Embodied / Robotics World Models

- **XPACE: Joint World and Action Modeling from Heterogeneous Experience** — *arXiv, 2026*
  [Paper](https://arxiv.org/abs/2609.17372) [Project](https://xpeng-robotics.github.io/xpace/)
  `World-Action Model` `Robotics` `Embodied AI` `Simulation` `Humanoid`
  XPACE is a unified embodied world model for humanoid robots that serves as both a world action model (jointly predicting actions and future video) and a world simulator.

### General Video World Models

- **HOLO-WORLD: Unified Camera, Object and Weather Control for Video World Model** — *arXiv, 2026*
  [Paper](https://arxiv.org/abs/2606.20083) [Project](https://xiangchenyin.github.io/Holo-World/)
  `Video World Model` `Controllable Generation` `Weather` `Camera Control` `Diffusion`
  Holo-World is a unified controllable video world model that jointly controls camera motion, object dynamics, and weather state from a single image.

<!-- PAPERS_END -->

## Contributing

Contributions are welcome! Please open a pull request to add new papers.

When adding a paper, please include:
- Title
- Authors
- Year
- Venue (arXiv / conference / journal)
- Paper link
- Code link (if available)
- Project page (if available)
- A brief one-sentence summary

## Maintenance

The paper list is generated from `data/papers.yaml`. After editing the YAML, run:

```bash
pip install -r requirements.txt
python scripts/generate_readme.py
```

The script only updates the content between the `<!-- PAPERS_START -->` and `<!-- PAPERS_END -->` markers; all other sections are preserved.
