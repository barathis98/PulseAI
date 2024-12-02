import os
from dotenv import load_dotenv
from openai import OpenAI
from pdf_extractor import extract_pdf_text_as_documents
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  
)

pdf_path = "data/Physiology.pdf"

pdf_documents = extract_pdf_text_as_documents(pdf_path)


text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(pdf_documents)

embedding = OpenAIEmbeddings()

db = Chroma.from_documents(documents, embedding, persist_directory = "chroma_db")

db.persist()

print("Vector store created and persisted.")
