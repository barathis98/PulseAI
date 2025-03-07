from langchain_community.document_loaders import PyPDFLoader
from langchain.schema import Document
def extract_pdf_text_as_documents(pdf_path: str):
    try:
        loader = PyPDFLoader(pdf_path)
        pages = loader.load()
        documents = [Document(page_content=page.page_content) for page in pages]
        return documents
    except Exception as e:
        print(f"Failed to process PDF: {e}")
        return []
