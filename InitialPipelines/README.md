# Phase 1: Early Baselines & Unimodal Experiments

This directory contains the **foundational experiments** designed to establish performance ceilings for individual modalities and test simple fusion architectures.

Each pipeline includes:  
* a core model/classifier  
* optional auxiliary models  
* an LLM reasoning layer  
* evaluation outputs

### Included Pipelines

| Notebook | Modality | Approach |
| :--- | :--- | :--- |
| **`Text_Only.ipynb`** | Text | **RoBERTa + LLM.** Uses a fine-tuned RoBERTa to detect fake headlines. Passes the prediction + confidence to GPT for a final verdict. |
| **`Visual_Only.ipynb`** | Vision | **CLIP + LLM.** Uses Zero-Shot CLIP with ImageNet/Places365 concepts to classify images without any textual context. |
| **`Image_to_Text.ipynb`** | I2T | **BLIP $\to$ RoBERTa.** Converts the image into a caption using BLIP, then treats it as a text classification problem. |
| **`Image_to_Text_Fusion.ipynb`** | Fusion | **User + AI Captions.** Compares the headline against the BLIP Caption. Uses semantic similarity (SentenceTransformer) to detect mismatches. |

### Experimental Goal

Before building complex agents, these pipelines answer the core question: *How much signal exists in the text vs. the image alone?*

---

👉 **[Go to Phase 2: Intermediate Pipelines (Agents)](../IntermediatePipelines)**
