from langchain_core.documents import Document

from backend.retrieval.hybrid_retriever import HybridRetriever


documents = [
    Document(
        page_content="Artificial Intelligence is transforming industries."
    ),
    Document(
        page_content="RAG combines retrieval and generation."
    ),
    Document(
        page_content="LangChain helps build LLM applications."
    ),
]

retriever = HybridRetriever(documents)

results = retriever.retrieve("What is RAG?")

for doc in results:
    print(doc.page_content)