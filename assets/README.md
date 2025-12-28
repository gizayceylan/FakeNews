# Project Artifacts & Dependencies

This directory contains **critical functional files**, precomputed embeddings, and the local image dataset required to run the detection pipelines.

These are not merely static resources; they are **loaded at runtime** to ensure reproducibility and bypass external dependencies (like dead URLs).

## File Manifest

| File | Type | Description |
| :--- | :--- | :--- |
| **`fakeddit_images.zip`** | **Archive** | Contains the 225 verified images. Pipelines unzip this at runtime to ensure every agent works on the exact same local image set. |
| **`fakeddit_balanced_subset.csv`** | **Metadata** | The master benchmark dataset (N=150) with a balanced 50/50 Fake/Real split used for final evaluation. |
| **`fakeddit_subset_blip2captions.csv`** | **Metadata** | The complete 225-sample subset enriched with pre-generated BLIP-2 captions. 
| **`fakeddit_subset.csv`** | **Metadata** | The raw subset data extracted from the larger Kaggle dataset. Kept as a fallback/reference. |
| **`concept_embeddings.npy`** | **Embeddings** | Precomputed embeddings for the CLIP vision tool. Allows the Vision Agent to search images instantly. |
| **`concepts_list.json`** | **Vocabulary** | The vocabulary list corresponding to the concept embeddings. |
| **`fakeddit_calibrated_sim_bins.json`** | **Calibration** | Calibration thresholds that allow agents to interpret raw similarity scores based on dataset statistics. |

---

## ⚠️ Usage Note
**Do not modify or delete these files.**
The notebooks rely on relative paths to these specific artifacts.
