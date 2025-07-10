import streamlit as st
import PyPDF2
import os
import sys

# Add root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.simplifier import load_glossary, simplify_text
from models.summarizer import summarize_text
from models.translator import translate_to_english  # ✅ Multilingual translation

# Page setup
st.set_page_config(page_title="LegalEase", layout="wide")
st.markdown("<h1 style='text-align: center;'>🧠 LegalEase</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>AI-Powered Legal Document Simplifier</h4>", unsafe_allow_html=True)
st.markdown("---")

# File uploader
uploaded_file = st.file_uploader("📄 Upload a legal document (PDF or TXT)", type=["pdf", "txt"])

# Read file
def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def read_txt(file):
    return file.read().decode("utf-8")

# State variables
doc_text = ""
summary = ""
simplified_text = ""

# Main logic
if uploaded_file:
    st.success("✅ File uploaded successfully!")

    if uploaded_file.type == "application/pdf":
        doc_text = read_pdf(uploaded_file)
    else:
        doc_text = read_txt(uploaded_file)

    # 🌍 Translate if needed
    with st.spinner("🌍 Detecting language and translating if needed..."):
        doc_text = translate_to_english(doc_text)

    tab1, tab2, tab3 = st.tabs(["📄 Original Text", "🧠 Summary", "📘 Simplified"])

    # Tab 1 – Original
    with tab1:
        st.subheader("📄 Original Document Text")
        st.text_area("Full Legal Document", doc_text, height=400)

    # Tab 2 – Summary
    with tab2:
        st.subheader("🧠 AI-Generated Summary")
        if st.button("🔍 Summarize with AI"):
            with st.spinner("Generating summary..."):
                summary = summarize_text(doc_text)
                st.success(summary)
                st.download_button("⬇️ Download Summary", summary, file_name="summary.txt", mime="text/plain")

    # Tab 3 – Simplified Text
    with tab3:
        st.subheader("📘 Simplified Legal Terms Output")
        if st.button("📘 Simplify Legal Terms"):
            with st.spinner("Simplifying..."):
                glossary_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "glossary", "legal_terms.json"))
                glossary = load_glossary(glossary_path)
                simplified_text = simplify_text(doc_text, glossary)
                st.info(simplified_text)
                st.download_button("⬇️ Download Simplified Version", simplified_text, file_name="simplified_output.txt", mime="text/plain")
else:
    st.info("📥 Please upload a legal document to get started.")
