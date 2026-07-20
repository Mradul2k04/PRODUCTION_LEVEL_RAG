from langchain_cohere import CohereEmbeddings
from backend.core.logger import logger
from backend.embeddings.base_embedding import BaseEmbedding
from backend.core.config import settings


class CohereEmbedding(BaseEmbedding):
    """
    Cohere Embedding Provider
    """
    def __init__(self):
        logger.info("Initializing Cohere Embedding Model...")

        self.embedding = CohereEmbeddings(
            model=settings.EMBED_MODEL,
            cohere_api_key=settings.COHERE_API_KEY
        )

        logger.info("Cohere Embedding Model initialized successfully.")

    def embed_documents(self, texts):
        try:
            logger.info(f"Generating embeddings for {len(texts)} documents.")
            return self.embedding.embed_documents(texts)

        except Exception as e:
            logger.exception(f"Error while generating document embeddings: {e}")
            raise

    def embed_query(self, text):
        try:
            logger.info("Generating query embedding.")
            return self.embedding.embed_query(text)

        except Exception as e:
            logger.exception(f"Error while generating query embedding: {e}")
            raise