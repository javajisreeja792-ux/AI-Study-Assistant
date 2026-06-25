import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai
from dotenv import load_dotenv
import os

from translations.languages import translations

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

# Language Selection
language = st.sidebar.selectbox(
    "Select Language",
    ["English", "Hindi", "Telugu"]
)

text = translations[language]

st.title(text["title"])

uploaded_file = st.file_uploader(
    text["upload"],
    type="pdf"
)

if uploaded_file:

    pdf_text = ""

    reader = PdfReader(uploaded_file)

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            pdf_text += extracted

    st.success(text["success"])

    question = st.text_input(
        text["question"]
    )

    if st.button(text["button"]):

        prompt = f"""
        Answer the question using the PDF.

        PDF:
        {pdf_text}

        Question:
        {question}
        """

        response = model.generate_content(prompt)

        st.write(response.text)
