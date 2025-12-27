# Intermediate Fusion Pipelines

This folder contains **intermediate fusion pipelines** that sit between the
early experimental baselines in `InitialPipelines/` and the planned final
multimodal agentic system.

All notebooks here use:

- a **single LLM** acting as an agent,
- multiple tools (vision, text, consistency),
- and a structured, phase-based reasoning prompt.

It currently includes:

- **Blind tool-using agent** – LLM cannot see the image, relies on tools.
- **Vision-enabled tool-using agent** – LLM sees the image + uses the same tools.

**Key Differences in Vision Version**

Compared to the **blind/tool-only** pipeline:

- The vision-enabled agent:
  - receives the **image directly** as part of the user message,
  - bases its **initial impression** on **image + headline** (instead of headline alone).
- The **Text Tool**:
  - now analyzes **only the headline** (no longer analyzes the BLIP-2 caption in this setup).
- The **Consistency Tool**:
  - keeps the **headline–caption** semantic similarity,
  - keeps the **image–headline** similarity,
  - **drops** the **image–caption** similarity term, because the agent can visually inspect the image itself.

As a result, this design **jointly probes two factors**:
  1. The contribution of **direct visual access** for the agent, and  
  2. The effect of **down-weighting noisy AI captions** in the tool stack.

The dataset and core models (CLIP, RoBERTa, MPNet, VADER) remain the same across both pipelines; what changes is **how strongly the caption enters the decision process** and whether the agent can "see" the image directly.

These pipelines serve as **intermediate baselines** to compare against both
simple unimodal models (CLIP, RoBERTa) and the future LangGraph-based system.
