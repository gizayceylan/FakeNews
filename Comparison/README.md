# Comparison of Selected Pipelines

This directory evaluates the progress of **five selected pipelines**, analyzing the critical trade-offs between **statistical performance** (Accuracy, Precision/Recall), **agentic reasoning**, and **detection speed**.

It includes the source code **[(notebooks)](./notebooks/)**, granular tool/agent performance metrics, and a comparative benchmark on a balanced Fakeddit subset (N=150).

## Pipeline Glossary

The following architectures were selected to represent key phases of the project's evolution:

| ID | Acronym | Description | Core Logic |
| :--- | :--- | :--- | :--- |
| **01** | **I2TFv1** | **Image-to-Text Fusion (Base)** | Fusion baseline using standard off-the-shelf models (Base RoBERTa, Base BLIP) + LLM reasoning. |
| **02** | **I2TFv2** | **Image-to-Text Fusion (Upgraded)** | Identical architecture to v1 but uses upgraded underlying models (e.g., Fakeddit-finetuned RoBERTa). |
| **03** | **SAFb** | **Blind Agent** | Single Agent that *cannot* see the image; relies only on tools/captions to reason. |
| **04** | **SAFv** | **Vision Agent** | Single Agent that *sees* the image directly + uses tools. |
| **05** | **MAH** | **Multi-Agent Hierarchy** | Panel of Experts (Vision, Text, Context) + Final Judge Agent. |

---

## Benchmark Results

Performance on Balanced Fakeddit Subset (75 Fake / 75 Real).

| Pipeline | Accuracy | Fake P/R | Real P/R | Counts (TP/FP/TN/FN) |
| :--- | :--- | :--- | :--- | :--- |
| **04_SAFv** | **0.833** | P=0.77, **R=0.96** | **P=0.95**, R=0.71 | 53 / 3 / 72 / 22 |
| **05_MAH** | 0.813 | **P=0.78**, R=0.87 | P=0.85, **R=0.76** | 57 / 10 / 65 / 18 |
| **02_I2TFv2** | 0.747 | P=0.67, **R=0.99** | **P=0.97**, R=0.51 | 38 / 1 / 74 / 37 |
| **03_SAFb** | 0.740 | P=0.66, R=0.97 | P=0.95, R=0.51 | 38 / 2 / 73 / 37 |
| **01_I2TFv1** | 0.600 | P=0.56, R=0.88 | P=0.73, R=0.32 | 24 / 9 / 66 / 51 |

*Note: TP=True Positive (Correct Real), TN=True Negative (Correct Fake).*

---

## Latency & Trade-offs

| Pipeline | Avg Runtime (sec/sample) | Use Case Recommendation |
| :--- | :--- | :--- |
| **02_I2TFv2** | **~1.51s** | **Real-Time Filtering.** Best for rapidly discarding obvious fakes before expensive processing. |
| **04_SAFv** | ~8.05s | **Maximum Detection.** Best for automated flagging systems where missing a fake is unacceptable. |
| **05_MAH** | ~12.09s | **Human Verification.** Best for providing a "Second Opinion" with detailed written explanations. |

## Key Insights

---

1.  **Direct Vision is Critical:** While the headline provides a strong veracity signal, relying solely on image captions (indirect vision) hits a performance ceiling. Detecting multimodal misinformation requires **direct visual perception** to verify subtle image-text conflicts effectively.
2.  **Simple Fusion is "Nervous":** Baseline fusion models (like I2TF) function well as **high-recall filters**—they catch almost all fakes but generate excessive false positives because they lack the reasoning capability to exonerate weird-but-real news.
3.  **The Interpretability Trade-off:** Increasing architectural complexity (moving from Single-Agent to Multi-Agent) yields a massive gain in **explainability and transparency**, but comes at a trade-off in processing speed.
4.  **Impact of Domain Specialization:** The performance jump in the baseline models demonstrates the value of using domain-specific tools (e.g., Fakeddit-trained classifiers) over generic ones. However, even specialized models have blind spots, which necessitates an **intelligent agent** to weigh these imperfect signals—or good **prompt engineering** to teach the nuance—rather than blindly trusting them.
