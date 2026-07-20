from langchain_core.documents import Document

from backend.services.rag_pipeline import RAGPipeline

documents = [
    Document(
        page_content="Artificial Intelligence enables machines to perform tasks that typically require human intelligence."
    ),
    Document(
        page_content="Retrieval-Augmented Generation (RAG) combines information retrieval with Large Language Models."
    ),
    Document(
        page_content="LangChain is a framework for building LLM applications."
    ),
]

pipeline = RAGPipeline(documents)

answer = pipeline.ask(
    "What is RAG?"
)

print(answer)