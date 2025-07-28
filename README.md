# Text Summarizer API (Python + Flask)

This repository contains a simple **text summarization API** built with Python, NLTK, and Flask.  
The API performs **extractive summarization** by analyzing word frequencies and selecting the most relevant sentences from the input text.

---

## Features
- Extractive summarization using NLTK
- Adjustable summary length (number of sentences)
- RESTful API built with Flask
- Ready to integrate with any frontend (e.g., Android app)

---

## Tech Stack
- **Python 3.9+**
- **Flask**
- **NLTK**

---

## Project Structure

- app.py # Main Flask app
- model.py # Summarization logic (extractive)
- setup_nltk.py # Download and prepare NLTK resources
- requirements.txt # Python dependencies
- README.md

---

## Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/text-summarizer-api.git
   cd text-summarizer-api
   
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
3. **Download NLTK data**
    ```bash
    python -m nltk.downloader punkt stopwords
    
4. Run the API
    ```bash
    python app.py
The API will run on:
http://127.0.0.1:5000

## Usage (Example with cURL)

### Endpoint
`/summarize`

### Method
`POST`

### Body (JSON)
    {
      "text": "Your long text goes here...",
      "num_sentences": 3
    }

### Response (JSON):
    {
      "summary": "Shortened summary text here...",
      "stats": {
        "original_word_count": 120,
        "summary_word_count": 40,
        "original_sentence_count": 8,
        "summary_sentence_count": 3
      }
    }
