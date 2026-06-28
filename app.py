import streamlit as st
from google import genai
from dotenv import load_dotenv
from pypdf import PdfReader
import os

# -------------------------
# Load API Key
# -------------------------
load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# -------------------------
# Languages (i18n)
# -------------------------
translations = {
    "English": {
        "title": "📚 AI Study Assistant",
        "upload": "Upload PDF",
        "question": "Ask a question about the PDF",
        "button": "Get Answer",
        "success": "PDF uploaded successfully!",
    },
    "Hindi": {
        "title": "📚 एआई अध्ययन सहायक",
        "upload": "पीडीएफ अपलोड करें",
        "question": "पीडीएफ के बारे में प्रश्न पूछें",
        "button": "उत्तर प्राप्त करें",
        "success": "पीडीएफ सफलतापूर्वक अपलोड हो गई!",
    },
    "Telugu": {
        "title": "📚 AI స్టడీ అసిస్టెంట్",
        "upload": "PDF అప్లోడ్ చేయండి",
        "question": "PDF గురించి ప్రశ్న అడగండి",
        "button": "సమాధానం పొందండి",
        "success": "PDF విజయవంతంగా అప్లోడ్ చేయబడింది!",
    },
}

# -------------------------
# Sidebar
# -------------------------
language = st.sidebar.selectbox("Select Language", ["English", "Hindi", "Telugu"])

text = translations[language]

# -------------------------
# Title
# -------------------------
st.title(text["title"])

# -------------------------
# Upload PDF
# -------------------------
uploaded_file = st.file_uploader(text["upload"], type=["pdf"])

if uploaded_file is not None:
    st.success(text["success"])

    # Read PDF
    reader = PdfReader(uploaded_file)

    pdf_text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            pdf_text += page_text

    # Limit text to avoid timeout
    pdf_text = pdf_text[:12000]

    # Ask Question
    question = st.text_input(text["question"])

    if st.button(text["button"]):
        if question.strip() == "":
            st.warning("Please enter a question.")
        else:
            prompt = f"""
Answer the following question using ONLY the PDF content.

Answer in {language}.

PDF Content:
{pdf_text}

Question:
{question}
"""

            with st.spinner("Generating answer..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-2.5-flash", contents=prompt
                    )

                    st.subheader("Answer")
                    st.write(response.text)

                except Exception as e:
                    st.error(f"Gemini Error: {e}")
