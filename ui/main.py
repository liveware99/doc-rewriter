
import streamlit as st
import pandas as pd
import requests

API_URL = "http://localhost:8000/rewrite-proposal"

st.set_page_config(page_title="Tech Proposal Rewriter", layout="centered")
st.title("📄 Technical Proposal Rewriter")

uploaded_file = st.file_uploader("Upload Compliance Sheet (.xlsx)", type=["xlsx"])

if uploaded_file:
    st.success("File uploaded. Click 'Start Rewriting' to preview editable content.")

    if st.button("Start Rewriting"):
        with st.spinner("Generating initial proposal content..."):
            files = {"file": (uploaded_file.name, uploaded_file, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
            response = requests.post(API_URL, files=files)

            if response.status_code == 200:
                st.success("Content rewritten. Download or edit below:")
                st.download_button(
                    label="📥 Download Final Proposal",
                    data=response.content,
                    file_name=f"final_{uploaded_file.name.replace('.xlsx', '.docx')}",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
            else:
                st.error("Rewrite failed. Please check backend logs.")
