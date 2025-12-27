# Comparison Notebooks

This directory contains the specific notebook implementations used to generate the comparative metrics between the different pipeline stages (Baseline vs. Single-Agent vs. Multi-Agent).

## ⚠️ Important Note on Scope

The notebooks in this folder are streamlined for **comparative analysis** and configured to run on a smaller balanced subset (e.g., N=150) for rapid benchmarking.

For **comprehensive documentation**, detailed architectural overviews, deep-dive observations, and experiments run on larger sample sizes, please refer to the dedicated source directories for each pipeline stage:

### Detailed Documentation Source

| Pipeline Stage | Directory | Description |
| :--- | :--- | :--- |
| **Phase 1: Baselines** | [**`../../EarlyPipelines`**](../../EarlyPipelines) | Early experiments to establish performance ceilings. Includes single-modality and fusion baseline analysis. |
| **Phase 2: Single-Agent** | [**`../../IntermediatePipelines`**](../../IntermediatePipelines) | Development of the Single-Agent Fusion (SAF) architecture. Includes "Blind" vs. "Vision" agent breakdowns and tool usage analysis. |
| **Phase 3: Multi-Agent** | [**`../../FinalPipelines`**](../../FinalPipelines) | The complete Multi-Agent Hierarchical (MAH) system. Contains the full system architecture and interpretability reports. |

---
