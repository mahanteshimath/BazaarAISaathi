import streamlit as st
from docling_core.types.doc.page import TextCellUnit
from docling_parse.pdf_parser import DoclingPdfParser, PdfDocument
from PIL import Image
import pytesseract
import os
import io
from utils.summariser import FinanceDocumentSummarizer

# Title of the app
st.title("Finance Document Summarizer")

# Initialize the summarizer
summarizer = FinanceDocumentSummarizer()

# Upload multiple files
uploaded_files = st.file_uploader("Upload files (PDF, PPT, Images, Text)", type=["pdf", "png", "jpg", "jpeg", "txt"], accept_multiple_files=True)

if uploaded_files:
    if st.button("Summarize"):
        for uploaded_file in uploaded_files:
            file_type = uploaded_file.type
            st.subheader(f"Processing File: {uploaded_file.name}")

            if file_type == "application/pdf":
                # Handle PDF files
                with open("temp.pdf", "wb") as f:
                    f.write(uploaded_file.getbuffer())

                summary = summarizer.summarize_pdf("temp.pdf")
                st.write("PDF summarization completed.")
                st.json(summary)  # Display the summary

            elif file_type in ["image/png", "image/jpeg", "image/jpg"]:
                # Handle image files
                with open("temp_image", "wb") as f:
                    f.write(uploaded_file.getbuffer())

                summary = summarizer.summarize_image("temp_image")
                st.write("Image summarization completed.")
                st.json(summary)  # Display the summary

            elif file_type == "text/plain":
                # Handle text files
                text_content = uploaded_file.read().decode("utf-8")
                summary = summarizer.summarize_text(text_content)
                st.write("Text summarization completed.")
                st.json(summary)  # Display the summary

            else:
                st.warning(f"Unsupported file type: {file_type}")

# Footer
footer = """<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #2C1E5B;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️ by <a style='display: inline; text-align: center;' href="https://www.linkedin.com/in/mahantesh-hiremath/" target="_blank">MAHANTESH HIREMATH</a></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
