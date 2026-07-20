from cohere import ClientV2
from langchain_core.documents import Document

from backend.core.logger import logger
from backend.core.config import settings


class CohereReranker:
    """
    Cohere Reranker implementation.
    """

    def __init__(self):
        logger.info("Initializing Cohere Reranker...")

        self.client = ClientV2(
            api_key=settings.COHERE_API_KEY
        )

        logger.info("Cohere Reranker initialized successfully.")

    def rerank(
        self,
        query: str,
        documents: list[Document],
        top_n: int = 3
    ) -> list[Document]:

        try:
            logger.info("Reranking retrieved documents...")

            texts = [
                doc.page_content
                for doc in documents
            ]

            response = self.client.rerank(
                model="rerank-v3.5",
                query=query,
                documents=texts,
                top_n=top_n
            )

            ranked_documents = []

            for result in response.results:
                ranked_documents.append(
                    documents[result.index]
                )

            logger.info(
                f"Top {len(ranked_documents)} documents selected."
            )

            return ranked_documents

        except Exception as e:
            logger.exception(f"Reranking failed: {e}")
            raise