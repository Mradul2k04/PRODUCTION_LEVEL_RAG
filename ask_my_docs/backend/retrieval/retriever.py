from langchain_core.documents import Document

from backend.vectorstore.vectorstore_factory import VectorStoreFactory
from backend.retrieval.base_retriever import BaseRetriever
from backend.core.logger import logger
from backend.core.config import settings


class VectorRetriever(BaseRetriever):
    """
    Vector Retriever using ChromaDB.
    """

    def __init__(self):
        logger.info("Initializing Vector Retriever...")

        self.vectorstore = VectorStoreFactory.get_vectorstore()

        logger.info("Vector Retriever initialized successfully.")

    def retrieve(
        self,
        query: str,
        k: int | None = None
    ) -> list[Document]:

        try:
            logger.info(f"Retrieving documents for query: {query}")

            return self.vectorstore.similarity_search(
                query=query,
                k=k or settings.TOP_K
            )

        except Exception as e:
            logger.exception(f"Error retrieving documents: {e}")
            raise

    def retrieve_with_score(
        self,
        query: str,
        k: int | None = None
    ) -> list[tuple[Document, float]]:

        try:
            logger.info(f"Retrieving documents with score for query: {query}")

            return self.vectorstore.similarity_search_with_score(
                query=query,
                k=k or settings.TOP_K
            )

        except Exception as e:
            logger.exception(f"Error retrieving documents with score: {e}")
            raise