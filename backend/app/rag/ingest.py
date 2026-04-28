from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import os


def ingest_document(file_path: str):
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(
        api_key=os.getenv("OPENROUTER_API_KEY")
    )

    vectordb = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory="chroma_db"
    )

    vectordb.persist()