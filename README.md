# 🕵️ **Agentic Systems for Multimodal Content Authenticity Verification**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![PyTorch](https://img.shields.io/badge/PyTorch-2.0-orange) ![Status](https://img.shields.io/badge/Status-Research_Preview-green)

## Table of Contents
1. [Introduction](#introduction)
2. [Problem Statement](#problem-statement)
3. [The Research Roadmap: Evolution of Agency (8 Pipelines)](#the-research-roadmap-evolution-of-agency-8-pipelines)
4. [Architectural Shift: From Synthesis to Decentralized Reasoning](#architectural-shift-from-synthesis-to-decentralized-reasoning)
5. [Evaluation Results](#evaluation-results)
6. [Repository Structure](#repository-structure)
7. [Setup Instructions](#setup-instructions)

---

## Introduction
Detecting misinformation in multimodal content (images + text) is a complex task that requires nuanced reasoning beyond simple classification. **Agentic Systems for Multimodal Content Authenticity Verification** is a comparative research project evaluating the evolution of AI agency in content forensics.

This project does not rely on static "black-box" classifiers for final verdicts. Instead, every pipeline developed—from the initial foundations to the final system—utilizes an **LLM Decision Agent**. This research documents the progression of these agents: from simple synthesizers of pre-computed signals to autonomous, tool-augmented investigators, and finally to a decentralized **Multi-Agent System (MAS)**.

---

## Problem Statement
Experimental observations across the development of these pipelines highlight three primary challenges in multimodal detection:

* **Modality Insufficiency**: Isolated modalities (Text-Only or Visual-Only) often lack the necessary context for reliable detection. Headlines are frequently too short to capture nuance, and visual cues alone can be too semantic-poor to support a confident verdict.
* **The Caption Bottleneck**: Relying on AI-generated image captions as a proxy for visual data (Indirect Vision) introduces information loss. Generic or incomplete captions can cause the agent to miss subtle contradictions between the image and the textual claim.
* **Reliability Gap in Fusion**: Standard fusion setups often struggle to reliably identify authentic news. Instead of denoising the signal, simple fusion can reinforce a "fake" bias, making it difficult for the system to trust legitimate but sensational content.

---

## The Research Roadmap: Evolution of Agency (8 Pipelines)

This project evaluated 8 distinct pipelines developed across three phases. While 7 pipelines represent the core evolutionary path, an upgraded version of the Fusion model (v2) was introduced during the comparison stage to analyze the impact of model performance on agentic decisions.

### **Phase 1: Early "Signal Synthesis" Agents (5 Pipelines)**
In this stage, the LLM acts as a synthesizer of pre-computed signals. It receives outputs from specific classifiers (RoBERTa, CLIP, ST Similarity) along with raw text (headline or caption) and renders a verdict based on short, direct prompts.
* **Pipelines:** `Text_Only`, `Visual_Only`, `Image_to_Text`, `Image_to_Text_Fusion (v1)`, and `I2TF (v2)`.
[**Image_to_Text_Fusion (v2):**](./Comparison/notebooks/02_I2TFv2.ipynb)

### **Phase 2: Intermediate Autonomous Agents (2 Pipelines)**
A shift toward autonomous agency using **LangChain**. These agents are not just fed signals; they are provided with specialized tools (Vision, Text, Context) and advanced prompting that guides them through phase-based reasoning and conflict resolution.
* **SAFb (Blind):** An agent that interrogates metadata and captions to see "indirectly."
* **SAFv (Vision):** An agent with direct access to a **Zero-Shot Vision Tool**, testing the impact of direct modality access on investigative accuracy.

### **Phase 3: Final Decentralized Multi-Agent System (1 Pipeline)**
The final architecture moves to a **Hierarchical "Panel of Experts."**
* [(**Multi-Agent Hierarchical (MAH)**)](./FinalPipelines/Multi_Agent_Hierarchical.ipynb) The workload is decentralized. Specialized forensic agents (Vision, Text, Context) work in parallel on their specific modalities and submit expert reports to a central **Judge Agent**. The Judge synthesizes these high-level reports to deliver a final verdict with deep reasoning.

---

## Architectural Shift: From Synthesis to Decentralized Reasoning

The primary technical contribution of this research is the documentation of how agentic workload and prompting affect reasoning quality.

1.  **Workload Optimization**: By moving from a single agent doing all the work (SAFv) to a multi-agent system (MAH), the task is decentralized. Modality-specific agents focus on their own evidence without being biased by other signals, while the Judge provides an objective synthesis.
2.  **Prompt Engineering Evolution**: Early prompts were limited to simple instructions. Intermediate and Final stages use carefully crafted prompts that include tool explanations, phase-based logic, and explicit conflict-solving recommendations.
3.  **Explainability vs. Accuracy**: While increasing complexity impacts processing time, it significantly improves the depth of the reasoning logs and the clarity of the user-facing "nudges."

---

## Evaluation Results
*Selected pipelines compared on a balanced (50/50) Fakeddit subset (N=150).*

| Pipeline | Accuracy | Fake Recall (Detection) | Decision Logic |
| :--- | :--- | :--- | :--- |
| **SAFv (Vision Agent)** | **0.833** | **0.96** | Direct Visual Investigation |
| **MAH (Multi-Agent)** | 0.813 | 0.87 | Decentralized Forensic Reports |
| **I2TFv2 (Baseline Fusion)** | 0.747 | 0.99 | Signal Synthesis (Aggressive) |

---

## Repository Structure

| Directory | Description |
| :--- | :--- |
| **[`Comparison/`](./Comparison/)** | Consolidated benchmarks, runtime logs, and the master comparison notebook for the 5 selected finalist pipelines. |
| **[`FinalPipelines/`](./FinalPipelines/)** | Source code for the decentralized **Multi-Agent Hierarchical (MAH)** system. |
| **[`IntermediatePipelines/`](./IntermediatePipelines/)** | Source code for the autonomous **SAFb** and **SAFv** single-agent frameworks. |
| **[`EarlyPipelines/`](./EarlyPipelines/)** | The foundational experiments using simple "Signal Synthesis" agents. |
| **[`preprocessing/`](./preprocessing/)** | The data foundry: EDA, CLIP embedding generation, BLIP-2 captioning, and tool calibration. |
| **[`assets/`](./assets/)** | Critical runtime artifacts (embeddings, image archives, calibration bins). |
| **[`Datasets/`](./Datasets/)** | Raw metadata and external vocabularies (ImageNet/Places365). |

---

## Setup Instructions

1.  **Configure API Keys**: Add your credentials to **`utils/api_key.py`**.
2.  **Verify Assets**: Ensure `fakeddit_images.zip` and `concept_embeddings.npy` are in the **`assets/`** directory.
3.  **Reproduce Benchmarks**: Open **`Comparison/Pipeline_Comparison.ipynb`** to view the consolidated performance metrics and charts.

---

## References
*Nakamura, K., et al. (2020). Fakeddit: A New Multimodal Benchmark Dataset for Fine-grained Fake News Detection.*
