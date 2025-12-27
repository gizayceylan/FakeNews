# Intermediate Fusion Pipelines (Single-Agent)

This directory contains **intermediate fusion pipelines** that sit between the experimental baselines in [`../EarlyPipelines/`](../EarlyPipelines/) and the final multi-agent system in [`../FinalPipelines/`](../FinalPipelines/).

All notebooks in this folder utilize a **Single-Agent Fusion (SAF)** approach featuring:
* a **single LLM** acting as the central reasoner,
* **multiple tools** (Vision, Text, Consistency) for evidence gathering,
* and a **structured prompt** that enforces a phase-based reasoning loop (*Intuition → Tools → Synthesis*).

## Included Pipelines

1.  **Blind Tool-Using Agent (`SAFb`)**
    * **Mechanism:** The LLM *cannot* see the image. It relies entirely on tool outputs (captions, CLIP scores) to understand visual content.
    * **Goal:** Establish a baseline for "reasoning without seeing."

2.  **Vision-Enabled Tool-Using Agent (`SAFv`)**
    * **Mechanism:** The LLM receives the **image directly** in the prompt alongside the same tools.
    * **Goal:** Measure the "Value of Vision" and the impact of reducing noise from captioning tools.

### Key Differences: Blind vs. Vision

The transition to the Vision-Enabled Agent involves specific architectural changes to reduce redundancy and noise:

| Feature | Blind Agent (`SAFb`) | Vision Agent (`SAFv`) |
| :--- | :--- | :--- |
| **Visual Access** | **None** (Relies on captions/tools) | **Direct** (Image embedded in user prompt) |
| **Initial Impression** | Based on **Headline only** | Based on **Image + Headline** |
| **Text Tool** | Analyzes Headline + **Caption** | Analyzes **Headline Only** (Reduces noise) |
| **Consistency Tool** | Measures Image↔Caption similarity | **Drops** Image↔Caption check (Redundant) |

> **Note:** The underlying core models (CLIP, RoBERTa, MPNet, VADER) remain constant across both pipelines

### Experimental Goal

This design is set up to jointly probe two critical factors:
1.  **The Value of Direct Perception:** Does giving the agent "eyes" outperform relying on converted text descriptions (captions)?
2.  **Noise Reduction:** Does down-weighting noisy AI-generated captions in the tool stack improve decision stability?

---

👉 **[Go to Phase 3: Final Pipelines (Multi-Agent)](../FinalPipelines)**
