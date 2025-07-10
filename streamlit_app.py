import streamlit as st
import os
import PyPDF2
from models.summarizer import summarize_text
from models.translator import translate_to_english
from utils.simplifier import simplify_legal_terms
import nltk
from langdetect import detect

nltk.download('punkt')

# 🌐 Load glossary for simplification
def load_glossary(path):
    import json
    with open(path, 'r') as f:
        return json.load(f)

# ✅ Fix path for Streamlit Cloud
glossary_path = os.path.join("glossary", "legal_terms.json")
glossary = load_glossary(glossary_path)

# 📄 Extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

# 🧠 Main app interface
st.set_page_config(page_title="LegalEase", layout="wide")
st.title("LegalEase: AI-Powered Legal Document Simplifier")

uploaded_file = st.file_uploader("Upload a legal document (PDF)", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Extracting and processing text..."):
        raw_text = extract_text_from_pdf(uploaded_file)
        st.subheader("📄 Extracted Text")
        st.write(raw_text)

        detected_lang = detect(raw_text)
        if detected_lang != 'en':
            with st.spinner("Translating to English..."):
                raw_text = translate_to_english(raw_text)
                st.success("Translation complete.")

        with st.spinner("Summarizing document..."):
            summary = summarize_text(raw_text)
            st.subheader("📝 Summary")
            st.write(summary)

        with st.spinner("Simplifying legal terms..."):
            simplified = simplify_legal_terms(summary, glossary)
            st.subheader("🔍 Simplified Summary")
            st.write(simplified)
