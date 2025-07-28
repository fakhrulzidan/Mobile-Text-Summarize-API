# setup_nltk.py

import nltk

def setup_nltk():
    try:
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        print("Error: NLTK data not found.")
        print("Run: python -m nltk.downloader punkt stopwords")
        exit()
