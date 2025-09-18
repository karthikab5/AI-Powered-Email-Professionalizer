# main.py
import streamlit as st
from email_engine import summarize_email
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=False)
import os
print("OPENAI_API_KEY present?", bool(os.getenv("OPENAI_API_KEY")))

st.title("📧 Email Summarizer")

# User pastes email
user_email = st.text_area("Paste your email:", height=200)

if st.button("Professionalize It To Me"):
    if user_email.strip():
        try:
            summary = summarize_email(user_email)
            st.subheader("Summary")
            st.write(summary)
        except Exception as e:
            st.error(f"Error while summarizing: {e}")
    else:
        st.warning("Please paste an email first.")
