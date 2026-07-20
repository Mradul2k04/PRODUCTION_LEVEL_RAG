from langchain_core.documents import Document

from backend.core.logger import logger
from backend.retrieval.base_retriever import BaseRetriever
from backend.retrieval.retriever import VectorRetriever
from backend.retrieval.bm25_retriever import BM25DocumentRetriever


class HybridRetriever(BaseRetriever):
    """
    Hybrid Retriever combining Vector Search and BM25.
    """

    def __init__(self, documents: list[Document]):
        logger.info("Initializing Hybrid Retriever...")

        self.vector_retriever = VectorRetriever()
        self.bm25_retriever = BM25DocumentRetriever(documents)

        logger.info("Hybrid Retriever initialized successfully.")

    def retrieve(
        self,
        query: str,
        k: int | None = None
    ) -> list[Document]:
        """
        Retrieve documents using both Vector Search and BM25.
        """
        try:
            logger.info(f"Hybrid retrieval for query: {query}")

            vector_docs = self.vector_retriever.retrieve(query, k)
            bm25_docs = self.bm25_retriever.retrieve(query, k)

            merged_docs = []
            seen = set()

            for doc in vector_docs + bm25_docs:
                if doc.page_content not in seen:
                    seen.add(doc.page_content)
                    merged_docs.append(doc)

            logger.info(
                f"Retrieved {len(merged_docs)} unique documents."
            )

            return merged_docs

        except Exception as e:
            logger.exception(f"Hybrid retrieval failed: {e}")
            raise

    def retrieve_with_score(
        self,
        query: str,
        k: int | None = None
    ):
        """
        Hybrid Retriever does not return scores.
        Use a reranker for final ranking.
        """
        raise NotImplementedError(
            "Hybrid Retriever does not support similarity scores."
        )