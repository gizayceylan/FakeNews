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

These pipelines serve as **intermediate baselines** to compare against both
simple unimodal models (CLIP, RoBERTa) and the future LangGraph-based system.
