import streamlit as st

st.set_page_config(page_title="Clinical NLP Toolkit", layout="wide")

st.title("🧬 Clinical NLP Toolkit")
st.markdown("""
Welcome to the **Clinical NLP Toolkit**!

Use the sidebar to navigate:

- 🩺 **Clinical Report Analyzer** to extract entities, classify, and identify key phrases in clinical reports.
- 💬 **Clinical Assistant Chatbot** to ask questions about your uploaded report.

Upload a `.txt` file in either tool to get started.
""")
