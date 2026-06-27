# 📚 AI Study Assistant

An AI-powered Study Assistant built using **Streamlit** and **Google Gemini AI**. The application allows users to upload PDF documents, ask questions about the content, generate notes, and take quizzes.

---

## Features

- 📄 Upload PDF documents
- 🤖 Ask questions about the uploaded PDF
- 📝 Generate study notes
- ❓ Generate quiz questions
- 🌐 Multilingual support (English, Hindi, Telugu)
- ⚡ Powered by Google Gemini AI

---

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- PyPDF
- python-dotenv

---

## Project Structure

```
AI-Study-Assistant/
│
├── app.py
├── requirements.txt
├── .gitignore
├── pages/
│   ├── notes.py
│   └── quiz.py
│
├── translations/
│   └── languages.py
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/javajisreeja792-ux/AI-Study-Assistant.git
```

Go to the project folder

```bash
cd AI-Study-Assistant
```

Install the dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

## Requirements

- Python 3.10+
- Google Gemini API Key

---

## Author

Sreeja Yadav
