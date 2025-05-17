import streamlit as st
from utils.tip_analysis import analyze_tip_or_advice
import tempfile

# Add docling import
try:
    from docling.ocr import ocr_image
    from docling.document_converter import DocumentConverter, PdfFormatOption
    from docling.datamodel.pipeline_options import PdfPipelineOptions
    from docling.datamodel.base_models import InputFormat
except ImportError:
    ocr_image = None
    DocumentConverter = None

st.title("Tip or Investment Advice Tester")
st.write("This app allows you to test the performance of your investment advice or tip. You can input the details of your investment, including the amount, duration, and expected return. The app will then calculate the potential profit or loss based on your inputs.")

# Add input for text-based advice
tip_text = st.text_area("Enter your investment advice or tip", placeholder="Type your investment advice or tip here...")

# Add file uploader for screenshot of advice
uploaded_file = st.file_uploader("Upload a screenshot of your investment advice (optional)", type=["png", "jpg", "jpeg"])

# Add input for PDF URL
pdf_url = st.text_input("Or enter a PDF URL to extract advice (optional)", placeholder="https://...")

pdf_extracted_text = None
if pdf_url and DocumentConverter is not None:
    try:
        pipeline_options = PdfPipelineOptions()
        pipeline_options.do_code_enrichment = True
        converter = DocumentConverter(format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        })
        with st.spinner("Extracting text from PDF..."):
            result = converter.convert(pdf_url)
            doc = result.document
            pdf_extracted_text = doc.text if hasattr(doc, "text") else str(doc)
        if pdf_extracted_text:
            st.subheader("Extracted Text from PDF:")
            st.write(pdf_extracted_text)
            if st.checkbox("Use extracted PDF text as tip/advice", key="pdf", value=True):
                tip_text = pdf_extracted_text
    except Exception as e:
        st.warning(f"Could not extract text from PDF: {e}")
elif pdf_url and DocumentConverter is None:
    st.warning("docling package is not installed. Please install it to enable PDF extraction functionality.")

extracted_text = None
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Screenshot", use_container_width=True)
    if ocr_image is not None:
        # Read image bytes and run OCR
        image_bytes = uploaded_file.read()
        try:
            # Save the uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                tmp.write(image_bytes)
                tmp_path = tmp.name
                extracted_text = ocr_image(tmp_path)
        except Exception as e:
            extracted_text = None
            st.warning(f"Could not extract text from image: {e}")
        if extracted_text:
            st.subheader("Extracted Text from Image:")
            st.write(extracted_text)
            # Optionally, allow user to use extracted text as tip_text
            if st.checkbox("Use extracted text as tip/advice", value=True):
                tip_text = extracted_text
    else:
        st.warning("docling package is not installed. Please install it to enable OCR functionality.")

if tip_text or uploaded_file:
    st.success("Your investment advice or tip has been submitted successfully!")

# Add a button to run deep analysis for the tip or advice
if st.button("Run Deep Analysis for Tip or Advice"):
    if tip_text:
        with st.spinner("Analyzing your tip or advice..."):
            api_key = st.secrets["PERPLEXITY_API_KEY"]
            analysis_result = analyze_tip_or_advice(tip_text, api_key)

            if isinstance(analysis_result, dict) and "error" in analysis_result:
                st.error(f"Error: {analysis_result['error']}")
            elif isinstance(analysis_result, dict):
                st.subheader("Deep Analysis Result")
                st.write(analysis_result.get("content", "No content available"))
            else:
                st.warning("Unexpected response format.")
    else:
        st.warning("Please enter a tip or advice before running the analysis.")

st.markdown(
    '''
    <style>
    .streamlit-expanderHeader {
        background-color: blue;
        color: white; /* Adjust this for expander header color */
    }
    .streamlit-expanderContent {
        background-color: blue;
        color: white; /* Expander content color */
    }
    </style>
    ''',
    unsafe_allow_html=True
)

footer="""<style>

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
<p>Developed with ❤️ by <a style='display: inline; text-align: center;' href="https://www.linkedin.com/in/mahantesh-hiremath/ " target="_blank">MAHANTESH HIREMATH</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)