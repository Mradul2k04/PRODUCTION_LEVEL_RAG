from backend.core.config import settings

from backend.embeddings.embedding_model import CohereEmbedding


class EmbeddingFactory:
    @staticmethod
    def get_embedding():

        if settings.EMBEDDING_PROVIDER.lower() == "cohere":
            return CohereEmbedding()

        raise ValueError(
            f"Unsupported Embedding Provider : {settings.EMBEDDING_PROVIDER}"
        )