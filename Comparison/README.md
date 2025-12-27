# Comparison of Selected Pipelines

This directory evaluates the progress of **five selected pipelines**, analyzing the critical trade-offs between **statistical performance** (Accuracy, Precision/Recall), **agentic reasoning**, and **detection speed**.

It includes full source code, granular tool/agent performance metrics, and a comparative benchmark on a balanced Fakeddit subset (N=150).

## Benchmark Results

Performance on Balanced Fakeddit Subset (75 Fake / 75 Real).

| Pipeline | Accuracy | Counts (TP/FP/TN/FN) | Fake P/R | Real P/R |
| :--- | :--- | :--- | :--- | :--- |
| **04_SAFv** | **0.833** | 53 / 3 / 72 / 22 | P=0.77, **R=0.96** | **P=0.95**, R=0.71 |
| **05_MAH** | 0.813 | 57 / 10 / 65 / 18 | **P=0.78**, R=0.87 | P=0.85, **R=0.76** |
| **02_I2TFv2** | 0.747 | 38 / 1 / 74 / 37 | P=0.67, **R=0.99** | **P=0.97**, R=0.51 |
| **03_SAFb** | 0.740 | 38 / 2 / 73 / 37 | P=0.66, R=0.97 | P=0.95, R=0.51 |
| **01_I2TFv1** | 0.600 | 24 / 9 / 66 / 51 | P=0.56, R=0.88 | P=0.73, R=0.32 |

*Note: TP=True Positive (Correct Real), TN=True Negative (Correct Fake).*

---

## Latency & Trade-offs

| Pipeline | Avg Runtime (sec/sample) | Use Case Recommendation |
| :--- | :--- | :--- |
| **02_I2TFv2** | **~1.51s** | **Real-Time Filtering.** Best for rapidly discarding obvious fakes. |
| **04_SAFv** | ~8.05s | **Maximum Detection.** Best for automated flagging systems where missing a fake is unacceptable. |
| **05_MAH** | ~12.09s | **Human Verification.** Best for providing a "Second Opinion" with detailed written explanations. |
