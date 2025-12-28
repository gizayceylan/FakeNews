# Data Preparation & Tool Calibration

This directory contains the foundational notebooks used to **construct the benchmark**, **calibrate agent tools**, and **pre-compute embeddings**.

These scripts are responsible for generating the functional artifacts stored in the **[`assets/`](../assets/)** folder. 

## Workflow & Notebooks

While these can be reviewed individually, they represent a logical pipeline for setting up the environment. To reproduce the project state from scratch, please follow this execution order:

| Order | Notebook | Purpose | Output (to `assets/`) |
| :--- | :--- | :--- | :--- |
| **01** | **`FakeNews_EDA.ipynb`** | **Exploration.** Initial analysis of the Fakeddit dataset structure, class balance, and image availability. | *Exploration only* |
| **02** | **`CleanMetadata_VisualConcepts.ipynb`** | **Vision Setup.** Generates the concept vocabulary and computes CLIP embeddings for the Zero-Shot tool. Provides initial subset metadata and creates the verified image archive. | `fakeddit_subset.csv`, `concepts_list.json`, `concept_embeddings.npy`, `fakeddit_images.zip` |
| **03** | **`Generate_BLIP2_Captions.ipynb`** | **Text Enrichment.** Runs the BLIP-2 model over the image archive to generate high-quality descriptive captions, providing subset metadata with generated captions. | `fakeddit_subset_blip2captions.csv` |
| **04** | **`Create_Balanced_Subset.ipynb`** | **Dataset Construction.** Processes the enriched metadata to filter for 2-way classes (Fake/Real) and creates the final balanced (50/50) benchmark subset used for evaluation. | `fakeddit_balanced_subset.csv` |
| **05** | **`Calibrate_Content_Similarity.ipynb`** | **Tool Calibration.** Calculates the distribution of cosine similarity scores (Text-to-Caption, Image-to-Text) on the final subset to define statistical thresholds for agent tools. | `fakeddit_calibrated_sim_bins.json` |

