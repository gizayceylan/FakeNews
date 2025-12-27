# Phase 3: Final Pipelines (Multi-Agent)

This directory contains the **final evolution** of the multimodal fake news detection system.

Building on the lessons from the Single-Agent experiments, this system distributes the reasoning load across specialized "Expert Agents" before a final "Judge agent" makes the verdict.

### Included Pipelines

* **Multi-Agent Hierarchical (`MAH`)**
    * The complete implementation of the hierarchical consensus system, built on **LangGraph**.
    * Uses a graph-based state machine to route information from the Experts to the Judge.
    * Includes the prompt engineering for all 4 LLM agents and the coordination logic.
 
### System Architecture: The Expert Panel

Instead of one LLM trying to do everything, **MAH** splits the task into distinct forensic roles. This mimics a human editorial board:

#### 1. The Experts (Level 1)
These agents run in parallel, each focusing on a single modality without being biased by the others.

* **Vision Agent:**
    * **Input:** Image only + Tool summary.
    * **Tools:** CLIP (Concept extraction), Zero-shot classification.
    * **Goal:** "Does this image look manipulated or inherently suspicious?"
* **Text Agent:**
    * **Input:** Headline only + Tool summary.
    * **Tools:** RoBERTa (Fakeddit-finetuned), VADER Sentiment Analysis.
    * **Goal:** "Is this headline clickbait, absurd, or malicious?"
* **Context Agent:**
    * **Input:** Image + Headline + Caption + Tool summary.
    * **Tools:** Similarity Checkers (Headline vs. Caption), Cross-modal retrieval (Image-Headline alignment).
    * **Goal:** "Does the image actually support the text, or is it unrelated?"

#### 2. The Judge (Level 2)
* **The Judge Agent:**
    * **Input:** Image + Headline + Three written reports from the Experts (not the raw tool results).
    * **Role:** Synthesizes the findings, resolves conflicts (e.g., "Text says Fake, Vision says Real"), and issues the final verdict.

---

### Experimental Goal

While Single-Agent models (`SAFv`) are accurate, they can be "black boxes." The MAH architecture solves this by design:

1.  **Interpretability:** There are **four distinct reports** explaining *exactly* what the Vision, Text, and Context experts found and how the Judge synthesized them to form the final verdict.
2.  **Conflict Resolution:** If the Text is sensational but the Image is benign, the Judge explicitly notes this discrepancy in the final reasoning.
3.  **Modularity:** Agents can be replaced without breaking the logic of the other agents.

---

👉 **[Go to Comparison Benchmarks](../Comparison)**
