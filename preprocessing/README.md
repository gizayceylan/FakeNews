# Data Preparation & Tool Calibration

This directory contains the foundational notebooks used to **construct the benchmark**, **calibrate agent tools**, and **pre-compute embeddings**.

These scripts are responsible for generating the artifacts stored in the `assets/` folder. 

## Workflow & Notebooks

While these can be reviewed individually, they represent a logical pipeline for setting up the environment:

| Notebook | Purpose | Output (to `assets/`) |
| :--- | :--- | :--- |
| **`FakeNews_EDA.ipynb`** | **Exploration.** Initial analysis of the Fakeddit dataset structure, class balance, and image availability. | *Analysis only* |
| **`Create_Balanced_Subset.ipynb`** | **Dataset Construction.** Downloads specific images, filters for valid links, and creates the balanced (50/50) benchmark csv. | `fakeddit_balanced_subset.csv`, `fakeddit_images.zip` |
| **`CleanMetadata_VisualConcepts.ipynb`** | **Vision Setup.** Generates the concept vocabulary and computes CLIP embeddings for the Zero-Shot tool. Also standardizes metadata. | `concept_embeddings.npy`, `concepts_list.json` |
| **`Generate_BLIP2_Captions.ipynb`** | **Text Enrichment.** Runs the BLIP-2 model over the image dataset to generate high-quality descriptive captions for the "Blind" agents. | `fakeddit_subset_blip2captions.csv` |
| **`Calibrate_Content_Similarity.ipynb`** | **Tool Calibration.** Calculates the distribution of cosine similarity scores (Text-to-Image, Text-to-Caption) to define statistical thresholds. | `fakeddit_calibrated_sim_bins.json` |

