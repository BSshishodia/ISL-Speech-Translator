# ISL-Speech-Translator
An AI-based system that converts Hindi speech into Indian Sign Language (ISL) videos using Whisper for speech recognition, NLP for text processing, and video synthesis for generating sign language output.

# 🎤 Hindi Speech to Indian Sign Language (ISL) Translator

## 🌟 Overview
This project is an AI-powered system that converts **Hindi speech into Indian Sign Language (ISL) videos**.

It is designed to bridge the communication gap between **hearing individuals and the deaf community** by transforming spoken language into visual sign representations.

---

## 💡 Why This Project?
Communication accessibility remains a major challenge for the deaf community, especially in regions where **Hindi is widely spoken**.

Most existing solutions:
- Focus on English or American Sign Language (ASL)
- Do not support Hindi speech
- Lack proper sign language structure

👉 This project addresses these gaps by providing a **Hindi-first ISL translation system**.

---

## ⚙️ How It Works

```markdown
## ⚙️ System Pipeline

flowchart TD
    A[🎤 Speech Input]
    B[🧾 Speech Recognition (Whisper)]
    C[🧠 NLP Processing]
    D[🔄 ISL Grammar Conversion]
    E[🌐 Hindi → English Mapping]
    F[🔍 Sign Matching]
    G[🎬 Video Generation]
    H[🤟 Final Output]

    A --> B --> C --> D --> E --> F --> G --> H
```
---

## 🧠 Core Components

### 🎤 Speech Recognition
- Uses Whisper model to convert Hindi audio into text  
- Supports multilingual and noisy audio input  

---

### 🧠 NLP Processing
- Tokenizes and cleans the text  
- Removes unnecessary words  
- Prepares sentence for ISL conversion  

---

### 🔄 ISL Grammar Conversion
- Converts Hindi sentence into ISL structure  
- Removes helper verbs and simplifies sentence  

---

### 🌐 Semantic Mapping
- Converts Hindi words into English concepts  
- Matches dataset labels for sign videos  

---

### 🔍 Sign Matching
- Uses fuzzy matching to find closest sign video  
- Works even with slight word variations  

---

### 🎬 Video Generation
- Combines multiple sign clips into a single output video  
- Creates smooth visual translation  

---

## 🛠️ Tech Stack

- Python  
- Whisper (Speech Recognition)  
- spaCy (Natural Language Processing)  
- MoviePy (Video Processing)  
- FFmpeg (Multimedia Handling)  
- difflib (Fuzzy Matching)  
- deep-translator (Language Translation)  

---

## 📁 Project Structure
```ISL-Speech-Translator/
│
├── app.py
├── speech_to_text.py
├── hindi_nlp.py
├── isl_converter.py
├── context_memory.py
│
├── dataset_loader.py
├── translator.py
├── sign_finder.py
├── video_merger.py
│
├── README.md
├── requirements.txt
├── .gitignore
```

---

## ▶️ How to Run

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
python app.py
