from backend.core.config import settings
from backend.vectorstore.chroma_store import ChromaStore


class VectorStoreFactory:
    """
    Factory class for vector databases.
    """

    @staticmethod
    def get_vectorstore():

        if settings.VECTOR_DB.lower() == "chroma":
            return ChromaStore()

        raise ValueError(
            f"Unsupported Vector Database: {settings.VECTOR_DB}"
        )