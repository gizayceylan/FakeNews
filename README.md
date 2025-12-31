# 🕵️ **Agentic Systems for Multimodal Content Authenticity Verification**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![PyTorch](https://img.shields.io/badge/PyTorch-2.0-orange) ![Status](https://img.shields.io/badge/Status-Research_Preview-green)

## Table of Contents
1. [Introduction](#introduction)
2. [Problem Statement](#problem-statement)
3. [The Research Roadmap: Evolution of Agency (3-Phases)](#the-research-roadmap-evolution-of-agency)
4. [Architectural Shift: From Synthesis to Decentralized Reasoning](#architectural-shift-from-synthesis-to-decentralized-reasoning)
5. [Selected Results](#selected-results)
6. [Performance Takeaways](#performance-takeaways)
7. [Future Work](#future-work)
8. [Repository Structure](#repository-structure)
9. [Setup Instructions](#setup-instructions)
10. [Citation & References](#citation--references)
11. [License](#license)

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

## The Research Roadmap: Evolution of Agency

This project evaluated 8 distinct pipelines developed across three phases, defined by the complexity of the architecture, agent's role and prompt engineering.

### **[Phase 1:](./EarlyPipelines/) Early "Signal Synthesis" Agents (5 Pipelines)**
In this stage, the LLM acts as a synthesizer of pre-computed signals. It receives outputs from specific models (RoBERTa, CLIP, BLIP, BLIP-2, SentenceTransformers) along with raw text (headline or caption) and renders a verdict based on short, direct prompts.
* [**Text_Only:**](./EarlyPipelines/Text_Only.ipynb) An agent evaluates content authenticity using only the headline and RoBERTa headline classification results.
* [**Visual_Only:**](./EarlyPipelines/Visual_Only.ipynb) An agent evaluates content authenticity using only CLIP-extracted visual concepts (indirect vision) and CLIP classification results.
* [**Image_to_Text:**](./EarlyPipelines/Image_to_Text.ipynb) An agent uses a BLIP-generated caption as a proxy for the image, treating multimodal verification as a text-only detection task and relies on RoBERTa caption classification results.
* [**Image_to_Text_Fusion (v1):**](./EarlyPipelines/Image_to_Text_Fusion.ipynb) An agent fuses headline and caption signals, RoBERTa classification results, and the cosine similarity score between headline and caption (via SentenceTransformer) to evaluate content authenticity.
* [**Image_to_Text_Fusion (v2):**](./Comparison/notebooks/02_I2TFv2.ipynb) An agent uses the same fusion workflow and logic as v1, but with BLIP-2 caption and domain-specific RoBERTa to isolate **model-choice effects** from fusion logic.

### **[Phase 2:](./IntermediatePipelines) Intermediate "Autonomous" Agents (2 Pipelines)**
A shift toward autonomous agency using **LangChain**. These agents are not just fed signals; they are provided with specialized tools (Vision, Text, Context) and advanced prompting that guides them through phase-based reasoning (intuition → tools → synthesis) and conflict resolution.
* [**Single-Agent Fusion-Blind (SAFb):**](./IntermediatePipelines/Single_Agent_Fusion_Blind.ipynb) An agent that cannot see the image directly and relies only on a headline to form an impression; uses tools and captions (indirect vision) to gather multimodal evidence; synthesizes all to provide a final decision, reasoning, and nudge.
* [**Single-Agent Fusion-Vision (SAFv):**](./IntermediatePipelines/Single_Agent_Fusion_Vision.ipynb) An agent with direct access to both image and headline content to form an impression; uses tools to gather more multimodal evidence; synthesizes all to provide a final decision, reasoning, and nudge.

### **[Phase 3:](./FinalPipelines) Final "Decentralized" Multi-Agent System (1 Pipeline)**
The final architecture moves to a **Hierarchical "Panel of Experts"**, built on **LangGraph**. Workload is divided among specialized agents guided through advanced prompting to follow phase-based reasoning.
* [**Multi-Agent Hierarchical (MAH):**](./FinalPipelines/Multi_Agent_Hierarchical.ipynb) The workload is decentralized. Specialized forensic agents (Vision, Text, Context) work independently on their specific modalities and submit expert reports to a central Judge Agent. The Judge synthesizes these high-level reports to deliver a final verdict with deep reasoning and user-facing nudge.

---

## Architectural Shift: From Synthesis to Decentralized Reasoning

The primary technical contribution of this research is the documentation of how agentic workload and prompting affect reasoning quality.

1.  **Workload Optimization**: By moving from a single agent doing all the work (SAFv) to a multi-agent system (MAH), the task is decentralized. Modality-specific agents focus on their own evidence without being biased by other signals, while the Judge provides an objective synthesis.
2.  **Prompt Engineering Evolution**: Early prompts were limited to simple instructions. Intermediate and Final stages use carefully crafted prompts that include tool explanations, phase-based logic, and explicit conflict-solving recommendations.
3.  **Explainability vs. Speed**: While increasing complexity impacts processing time, it significantly improves the depth of the reasoning logs and the clarity of the user-facing "nudges".

---

## Selected Results
*Compared on a class balanced Fakeddit subset (N=150; latency = sec/sample):*

| Pipeline | Phase | Latency | Accuracy | Fake P/R | Real P/R | Decision Logic |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **MAH (Multi-Agent)** | Final | ~12.09s | **0.813** | **P=0.78**, R=0.87 | P=0.85, **R=0.76** | Decentralized Expert Reports |
| **SAFv (Single-Agent)** | Intermediate | ~8.05s | **0.833** | P=0.77, **R=0.96** | **P=0.95**, R=0.71 | Direct Multimodal Investigation |
| **I2TFv2 (Baseline Fusion)** | Early | **~1.51s** | 0.747 | P=0.67, **R=0.99** | **P=0.97**, R=0.51 | Signal Synthesis (Aggressive) |

---

## Performance Takeaways

The benchmarks reveal a clear trade-off between speed, accuracy, and interpretability. Depending on the deployment needs, different pipelines serve different roles:

* **MAH (High Accuracy | Low Speed):** → Best for **human-in-the-loop verification**. While it has a higher "reasoning tax" (latency), it offers the most balanced recall and provides specialized reports that make verdicts auditable.
* **SAFv (High Accuracy | Moderate Speed):** → Best for **autonomous fake news detection**. By giving the agent "eyes", it achieves the best balance of identifying fakes without the complexity of a full multi-agent overhead.
* **I2TFv2 (Moderate Accuracy | High Speed):** → Best for **real-time filtering**. Its aggressive nature makes it an ideal first-line defense for screening massive content streams before passing suspicious cases to more advanced agents.

---

## Future Work
1.  **Refining Vision:** Replacing or re-scoping the vision component with a model upgrade (e.g., FastVLM) to enable direct image reasoning and contextual understanding, improving both speed and accuracy.
2.  **Reducing Latency:** Optimizing the multi-agent communication overhead to make it viable for real-time streams.
3.  **Web Search Integration:** Equipping an agent with live internet search capabilities to verify breaking news events against trusted external sources and fact-checking databases.
4.  **Human-in-the-Loop:** Building a UI where the agent presents its evidence to a human moderator for final approval.

---

## Repository Structure

| Directory | Description |
| :--- | :--- |
| **[`assets/`](./assets/)** | Critical runtime artifacts (embeddings, image archives, calibration bins). |
| **[`Comparison/`](./Comparison/)** | Consolidated benchmarks, runtime logs, and the master comparison notebook for the 5 selected finalist pipelines. |
| **[`Datasets/`](./Datasets/)** | Raw metadata and external vocabularies (ImageNet/Places365). |
| **[`EarlyPipelines/`](./EarlyPipelines/)** | The foundational experiments using simple "Signal Synthesis" agents. |
| **[`IntermediatePipelines/`](./IntermediatePipelines/)** | Source code for the autonomous SAFb and SAFv single-agent systems. |
| **[`FinalPipelines/`](./FinalPipelines/)** | Source code for the decentralized MAH multi-agent system. |
| **[`preprocessing/`](./preprocessing/)** | The data foundry: EDA, CLIP embedding generation, BLIP-2 captioning, and tool calibration. |
| **[`utils/`](./utils/)** | Contains utility script for secure API client management across different environments (Local/Colab). |

---

## Setup Instructions

### 1. Repository Initialization

First, clone the repository and navigate into the project folder to ensure all notebooks correctly resolve relative paths for utilities and assets.

```bash
!git clone https://github.com/gizayceylan/FakeNews.git
%cd FakeNews
```

### 2. General Model Dependencies

This project requires **Python 3.10+**. The following command installs the libraries needed for specialized models and agentic frameworks.

```bash
# Specialized Models
!pip install -q transformers sentence-transformers vaderSentiment openai torch torchvision 

# Agentic Orchestration
!pip install -q langgraph langchain-openai langchain-community
```
> [!NOTE]
> Each notebook in this project includes local setup instructions specific to its architecture. While GPU is recommended for vision models (BLIP/BLIP-2/CLIP), the repo can still be explored on CPU with higher latency.

### 3. Environment Compatibility (SAFb & SAFv Only)  
The Phase 2 pipelines (**SAFb** and **SAFv**) utilize **LangChain Legacy Agents**. These are highly sensitive to version conflicts with default packages in environments like Google Colab.

> [!IMPORTANT]
> For Phase 2 agents, you **must** follow the specialized "Uninstall & Reinstall" sequence provided inside those specific notebooks. This ensures the environment is downgraded correctly to support legacy agent logic.

### 4. API Configuration
The agents require an OpenAI API key. The project includes a secure utility in `utils/api_key.py` to handle credentialing:

* **Google Colab:** Add your key to the **Secrets** tab (🔑) with the name `OPENAI_API_KEY`.
* **Local Environment:** Set the environment variable `export OPENAI_API_KEY='your-key-here'`.
* **Fallback:** If no key is detected, the system will securely prompt you for one at runtime.

### 5. Artifacts
Ensure the artifacts are present in the [`assets/`](./assets/) directory (these are loaded automatically by the notebooks).

### 6. Quick Start
The project is organized by the level of agentic complexity. You can explore the research by running the notebooks in their respective directories:

* **Early Baselines**: [`EarlyPipelines/`](./EarlyPipelines/)  
* **Tool-Using Agents**: [`IntermediatePipelines/`](./IntermediatePipelines/)  
* **Multi-Agent System**: [`FinalPipelines/`](./FinalPipelines/)  
* **Comparison Pipelines**: [`Comparison/notebooks/`](./Comparison/notebooks/)  
  *Run the [**Pipeline_Comparison.ipynb**](./Comparison/Pipeline_Comparison.ipynb) to reproduce the head-to-head metrics across all phases.*

---

## Citation & References

If you use this work, please cite it as below:


```bibtex
@software{ceylan_fakenews_2025,
  author = {Ceylan, Gizay},
  title = {{Agentic Systems for Multimodal Content Authenticity Verification}},
  url = {https://github.com/gizayceylan/FakeNews},
  version = {1.0.0},
  year = {2025}
}
```

If you use Fakeddit dataset, please cite it as follows, per creators' official request:


```bibtex
@article{nakamura2019r,
    title={r/Fakeddit: A New Multimodal Benchmark Dataset for Fine-grained Fake News Detection},
    author={Nakamura, Kai and Levy, Sharon and Wang, William Yang},
    journal={arXiv preprint arXiv:1911.03854},
    year={2019}
}
```

---

## License

See [`LICENSE`](LICENSE).
