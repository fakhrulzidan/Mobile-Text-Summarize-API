# model.py

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest
# from PyPDF2 import PdfReader
# import docx

def summarize_text(text, num_sentences):
    sentences = sent_tokenize(text)
    if not sentences:
        return "", {}

    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    punctuation = set(['.', ',', '!', '?', ';', ':', '"', "'", '(', ')', '[', ']', '{', '}'])
    stop_words.update(punctuation)
    filtered_words = [word for word in words if word not in stop_words]

    word_frequencies = {}
    for word in filtered_words:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1

    sentence_scores = {}
    for sentence in sentences:
        sentence_words = word_tokenize(sentence.lower())
        score = sum(word_frequencies.get(word, 0) for word in sentence_words)
        sentence_scores[sentence] = score / len(sentence_words) if sentence_words else 0

    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    ordered_summary = [sent for sent in sentences if sent in summary_sentences]
    summary = ' '.join(ordered_summary)

    stats = {
        "original_char_count": len(text),
        "original_word_count": len(words),
        "original_sentence_count": len(sentences),
        "summary_char_count": len(summary),
        "summary_word_count": len(word_tokenize(summary)),
        "summary_sentence_count": len(summary_sentences),
    }

    return summary, stats

# def extract_text_from_pdf(file):
#     reader = PdfReader(file)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text() or ""
#     return text

# def extract_text_from_docx(file):
#     doc = docx.Document(file)
#     text = "\n".join([para.text for para in doc.paragraphs])
#     return text