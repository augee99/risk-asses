from crewai_tools import BaseTool
from PyPDF2 import PdfReader
from pydantic import Field  # Import for adding metadata or defaults

class PDFReaderTool(BaseTool):
    """
    A tool for interacting with PDF files.
    """
    
    name: str = "PDFReaderTool"
    description: str = "Reads PDF File"
    pdf_path: str = Field(..., description="Path to the PDF file")  # Field is required

    def _run(self, query: str):
        return self.extract_text()

    def extract_text(self) -> str:

        try:
            with open(self.pdf_path, 'rb') as pdf_file:
                reader = PdfReader(pdf_file)
                text = ""
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    text += page.extract_text()
                return text
        except Exception as e:
            return f"Error extracting text from PDF: {e}"

    def get_page_count(self) -> int:

        try:
            with open(self.pdf_path, 'rb') as pdf_file:
                reader = PdfReader(pdf_file)
                return len(reader.pages)
        except Exception as e:
            return f"Error getting page count: {e}"
