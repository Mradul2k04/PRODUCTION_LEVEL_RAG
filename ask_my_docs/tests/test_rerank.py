from langchain_core.documents import Document

from backend.reranker.reranker import CohereReranker

docs = [
    Document(page_content="Artificial Intelligence is transforming industries."),
    Document(page_content="RAG combines retrieval and generation."),
    Document(page_content="LangChain helps build LLM applications."),
]

reranker = CohereReranker()

results = reranker.rerank(
    query="What is RAG?",
    documents=docs,
    top_n=2
)

for doc in results:
    print(doc.page_content)