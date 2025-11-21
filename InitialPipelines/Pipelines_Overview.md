
# Fake News Detection — Initial Pipelines Overview

This document summarizes the initial pipelines developed for the multimodal misinformation detection project.  
Each pipeline includes:  
- A core model or classifier  
- Optional auxiliary models  
- An LLM reasoning layer  
- Evaluation outputs

---

## 1. Text-Only Pipeline

### **Goal**  
Classify whether a news headline is real or fake, using text only.

### **Approach**
1. Use a pretrained **RoBERTa** as a classifier to predict *fake/real* user captions.
2. Extract prediction label + confidence.
3. Pass results to **GPT-4.1 Mini** for reasoning:
  - Provide decision (Real/Fake/Unclear)
  - Provide explanation
  - Suggest an action (nudge)

### **Components**
- `roberta-base-openai-detector`
- GPT-4.1 Mini (LLM reasoning)
- Standard text preprocessing

### **Evaluation**
- Accuracy of classifier + LLM  
- Confusion matrices  
- Classification reports  

---

## 2. Image-Only Pipeline

### **Goal**  
Detect misinformation from the image alone (no textual input).

### **Approach**
1. Extract **CLIP image embeddings**.
2. Compute **Top-K visual concepts** (ImageNet + Places365 labels).
3. Train a lightweight **Logistic Regression classifier** on the embeddings.
4. Provide classifier outputs to GPT-4.1 Mini:
   - Top-K visual concepts
   - Image classifier prediction (real/fake)
   - Confidence score
5. LLM provides decision, explanation, and nudge.

### **Components**
- CLIP ViT-B/32 image encoder  
- Logistic Regression classifier  
- GPT-4.1 Mini (reasoning)

### **Evaluation**
- Accuracy of classifier + LLM
- Confusion matrices  
- Classification reports  

---

## 3. Image-to-Text Pipeline 

### **Goal**  
Detect misinformation by converting the image into a caption, then analyzing the caption.

### **Approach**
1. Use **BLIP** to generate a caption for the image.  
2. Classify the caption using **RoBERTa**.  
3. Pass BLIP caption + classifier prediction + confidence to GPT-4.1 Mini.  
4. LLM provides decision, explanation, and nudge.

### **Components**
- BLIP image captioning model  
- RoBERTa fake-news detector  
- GPT-4.1 Mini (reasoning)

### **Evaluation**
- Accuracy of classifier + LLM 
- Confusion matrices  
- Classification reports  

---

## 4. Basic Multimodal Pipeline 

### **Goal**  
Build a lightweight multimodal system combining user-provided captions and BLIP-generated captions.

### **Approach**
1. **User caption (ground truth text)**  
   - RoBERTa prediction + confidence  
2. **BLIP caption**  
   - RoBERTa prediction + confidence  
3. **Semantic similarity** between user + BLIP captions  
   - Using SentenceTransformer (all-mpnet-base-v2)  
4. Provide ALL signals to GPT-4.1 Mini for final reasoning:  
   - Two captions  
   - Two classifier predictions  
   - Two confidence scores  
   - Similarity score  
5. LLM provides decision, explanation, and nudge.

### **Components**
- BLIP image captioning model  
- RoBERTa fake-news detector  
- SentenceTransformer similarity model  
- GPT-4.1 Mini (multimodal reasoning)

### **Evaluation**
- Accuracy of both classifiers + LLM  
- Confusion matrices (user, BLIP, LLM)  
- Pairwise similarity matrix  
- Classification reports  

---

## Next Steps 

These are planned for the following development phase:

### **Full Multimodal Orchestrator** (to-be-updated)
Combining:
- CLIP image concepts  
- Image classifier output  
- User text  
- BLIP caption  
- Text classifiers  
- Cross-modal similarity  
- Multimodal LLM reasoning  

### **FastVLM experiments**
A new vision-language model for improved speed/accuracy.

### **Streamlit Interface**
Interactive demo for:
- Uploading images  
- Providing captions  
- Viewing model decisions  
- Transparency/explanations  

