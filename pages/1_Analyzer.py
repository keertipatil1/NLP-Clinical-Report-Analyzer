import streamlit as st
from analyzer.ner import analyze_report
from analyzer.utils import clean_text
from analyzer.classifier import classify_report
from analyzer.phrases import extract_key_phrases

st.set_page_config(page_title="Clinical Report Analyzer", layout="wide")
st.title("🩺 Clinical Report Analyzer")

uploaded_file = st.file_uploader("Upload Clinical Report (.txt)", type=["txt"])

if uploaded_file:
    raw_text = uploaded_file.read().decode("utf-8")
    st.subheader("📄 Original Report")
    st.text(raw_text)

    cleaned_text = clean_text(raw_text)

    # Named Entity Recognition
    results = analyze_report(cleaned_text)
    st.subheader("🧠 Extracted Entities")
    for entity in results:
        st.markdown(f"**{entity['text']}** — *{entity['label']}*")

    # Classification
    st.subheader("📑 Report Classification")
    category = classify_report(cleaned_text)
    st.success(f"This report is classified under **{category}**")

    # Key Phrase Extraction
    st.subheader("📌 Key Phrases")
    phrases = extract_key_phrases(cleaned_text)
    st.write(phrases)
