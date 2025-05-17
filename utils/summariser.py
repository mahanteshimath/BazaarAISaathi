import pytesseract
from PIL import Image
from docling_parse.pdf_parser import DoclingPdfParser, PdfDocument
from docling_core.types.doc.page import TextCellUnit

class FinanceDocumentSummarizer:
    """A class to summarize finance documents including PDFs, images, and text files."""

    def summarize_pdf(self, pdf_path):
        """Summarize the given PDF file.

        Args:
            pdf_path (str): The file path to the PDF document.

        Returns:
            list: A list of dictionaries containing the summary of each page.
        """
        parser = DoclingPdfParser()
        pdf_doc: PdfDocument = parser.load(path_or_stream=pdf_path)
        summary = []

        for page_no, pred_page in pdf_doc.iterate_pages():
            page_summary = {
                "page_number": page_no,
                "words": [
                    {"rect": word.rect, "text": word.text}
                    for word in pred_page.iterate_cells(unit_type=TextCellUnit.WORD)
                ]
            }
            summary.append(page_summary)

        return summary

    def summarize_image(self, image_path):
        """Summarize the given image file.

        Args:
            image_path (str): The file path to the image.

        Returns:
            dict: A dictionary containing the extracted text or an error message.
        """
        image = Image.open(image_path)
        try:
            extracted_text = pytesseract.image_to_string(image)
            return {"text": extracted_text}
        except Exception as e:
            return {"error": str(e)}

    def summarize_text(self, text_content):
        """Summarize the given text content.

        Args:
            text_content (str): The text content to summarize.

        Returns:
            dict: A dictionary containing the text content.
        """
        return {"text": text_content}
