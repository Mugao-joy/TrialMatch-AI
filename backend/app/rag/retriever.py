from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import os


def retrieve_context(query: str):
    embeddings = OpenAIEmbeddings(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url=os.getenv("OPENROUTER_BASE_URL"),
        model="text-embedding-3-small",
    )

    vectordb = Chroma(
        persist_directory="app/rag/chroma_db",
        embedding_function=embeddings,
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    docs = retriever.invoke(query)

    return "\n\n".join([doc.page_content for doc in docs])