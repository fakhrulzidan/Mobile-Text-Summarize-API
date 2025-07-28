from flask import Flask, request, jsonify
from setup_nltk import setup_nltk
from models import summarize_text

app = Flask(__name__)
setup_nltk()  

@app.route("/")
def home():
    return "Text Summarizer API is running."

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json

    text = data.get("text", "")
    num_sentences = int(data.get("num_sentences", 3))

    if not text.strip():
        return jsonify({"error": "Text is empty"}), 400

    summary, stats = summarize_text(text, num_sentences)

    return jsonify({
        "summary": summary,
        "stats": stats
    })

if __name__ == "__main__":
    app.run(debug=True)
