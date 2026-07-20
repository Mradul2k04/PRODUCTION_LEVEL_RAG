from langchain_community.retrievers import BM25Retriever

from backend.core.logger import logger
from backend.retrieval.base_retriever import BaseRetriever
from langchain_core.documents import Document


class BM25DocumentRetriever(BaseRetriever):
    """
    BM25 Retriever implementation.
    """

    def __init__(self, documents: list[Document]):
        logger.info("Initializing BM25 Retriever...")

        self.retriever = BM25Retriever.from_documents(documents)

        logger.info("BM25 Retriever initialized successfully.")

    def retrieve(
        self,
        query: str,
        k: int | None = None
    ) -> list[Document]:

        try:
            logger.info(f"Retrieving documents using BM25 for query: {query}")

            if k:
                self.retriever.k = k

            return self.retriever.invoke(query)

        except Exception as e:
            logger.exception(f"BM25 retrieval failed: {e}")
            raise

    def retrieve_with_score(
        self,
        query: str,
        k: int | None = None
    ):
        """
        BM25Retriever in LangChain does not return similarity scores.
        """
        raise NotImplementedError(
            "BM25Retriever does not support similarity scores."
        )