import streamlit as st
from analyzer.utils import clean_text
from analyzer.chatbot import generate_response

st.set_page_config(page_title="Clinical Assistant Chatbot")
st.title("💬 Clinical Assistant Chatbot")

uploaded_file = st.file_uploader("Upload Clinical Report (.txt)", type=["txt"])

if uploaded_file:
    raw_text = uploaded_file.read().decode("utf-8")
    cleaned_text = clean_text(raw_text)
    st.subheader("📄 Chat Based on Report")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_query = st.text_input("Ask me anything about the report...")

    if user_query:
        response = generate_response(user_query, cleaned_text)
        st.session_state.chat_history.append(("You", user_query))
        st.session_state.chat_history.append(("Assistant", response))

    for speaker, msg in st.session_state.chat_history:
        st.markdown(f"**{speaker}:** {msg}")
