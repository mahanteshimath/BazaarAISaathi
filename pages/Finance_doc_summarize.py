import streamlit as st
from docling_core.types.doc.page import TextCellUnit
from docling_parse.pdf_parser import DoclingPdfParser, PdfDocument
from PIL import Image
import pytesseract
import os
import io

# Title of the app
st.title("Finance Document Summarizer")

# Upload multiple files
uploaded_files = st.file_uploader("Upload files (PDF, PPT, Images, Text)", type=["pdf", "png", "jpg", "jpeg", "txt"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        file_type = uploaded_file.type
        st.subheader(f"Processing File: {uploaded_file.name}")

        if file_type == "application/pdf":
            # Handle PDF files
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.getbuffer())

            parser = DoclingPdfParser()
            pdf_doc: PdfDocument = parser.load(path_or_stream="temp.pdf")

            st.write("Parsing PDF...")

            for page_no, pred_page in pdf_doc.iterate_pages():
                st.subheader(f"Page {page_no}")

                # Display extracted words with coordinates
                st.write("### Word-level Extraction")
                for word in pred_page.iterate_cells(unit_type=TextCellUnit.WORD):
                    st.text(f"{word.rect}: {word.text}")

                # Render image of characters
                st.write("### Character-level Image")
                img = pred_page.render_as_image(cell_unit=TextCellUnit.CHAR)
                st.image(img, caption=f"Rendered Characters - Page {page_no}")

        elif file_type in ["image/png", "image/jpeg", "image/jpg"]:
            # Handle image files
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)

            try:
                # Extract text using pytesseract
                extracted_text = pytesseract.image_to_string(image)
                st.write("### Extracted Text from Image:")
                st.text(extracted_text)
            except Exception as e:
                st.error(f"Error extracting text from image: {e}")

        elif file_type == "text/plain":
            # Handle text files
            text_content = uploaded_file.read().decode("utf-8")
            st.write("### Text File Content:")
            st.text(text_content)

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
