# 🌈 Resume Ranker

### 🔍 Description
Resume Ranker is a web-based application that ranks uploaded resumes based on their keyword similarity with a given job description using **TF-IDF and cosine similarity**.

---

## 💻 Tech Stack
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python (Flask)  
- **Libraries:** scikit-learn, PyMuPDF, python-docx  

---

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/resume-ranker.git
   cd resume-ranker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open in browser:
   ```
   http://127.0.0.1:5000
   ```

---

## ☁️ Deployment on Render
1. Create a free account on [https://render.com](https://render.com).  
2. Connect your GitHub repo.  
3. Build Command:  
   ```bash
   pip install -r requirements.txt
   ```
4. Start Command:  
   ```bash
   python app.py
   ```
5. Deploy and use the generated public URL.

---

## 🧩 Example Output
| Rank | Filename | Score | Snippet |
|------|-----------|--------|---------|
| 1 | resume1.pdf | 0.92 | Lorem ipsum dolor sit amet... |
| 2 | resume2.docx | 0.78 | Proin tincidunt vel orci... |

---

## 📜 License
MIT License – Free to use and modify.
