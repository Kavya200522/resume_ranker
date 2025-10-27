from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import fitz  # PyMuPDF
import docx
import io

app = Flask(__name__, static_folder="static", template_folder="templates")

def extract_text(file_storage):
    filename = file_storage.filename.lower()
    data = file_storage.read()
    text = ""
    if filename.endswith(".pdf"):
        pdf = fitz.open(stream=data, filetype="pdf")
        for page in pdf:
            text += page.get_text("text")
    elif filename.endswith(".docx"):
        doc = docx.Document(io.BytesIO(data))
        text = "\n".join([p.text for p in doc.paragraphs])
    elif filename.endswith(".txt"):
        text = data.decode("utf-8", errors="ignore")
    return text.strip()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/rank/keyword", methods=["POST"])
def rank_keyword():
    job_desc = request.form.get("job_description", "").strip()
    files = request.files.getlist("resumes[]")
    if not job_desc or not files:
        return jsonify({"error": "Missing job description or resumes"}), 400

    texts, filenames = [], []
    for f in files:
        text = extract_text(f)
        if text:
            texts.append(text)
            filenames.append(f.filename)

    corpus = [job_desc] + texts
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    results = []
    for name, score, content in zip(filenames, similarities, texts):
        snippet = content[:200].replace("\n", " ") + "..."
        results.append({
            "filename": name,
            "score": round(float(score), 3),
            "snippet": snippet
        })
    results.sort(key=lambda x: x["score"], reverse=True)
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
