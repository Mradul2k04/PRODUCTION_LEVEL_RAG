from pathlib import Path

from backend.core.logger import logger
from backend.loaders.loader_factory import LoaderFactory
from backend.chunking.chunker import DocumentChunker
from backend.vectorstore.vectorstore_factory import VectorStoreFactory


class IngestionPipeline:
    """
    Pipeline responsible for loading, chunking,
    embedding and storing documents.
    """

    def __init__(self):

        logger.info("Initializing Ingestion Pipeline...")

        self.chunker = DocumentChunker()
        self.vectorstore = VectorStoreFactory.get_vectorstore()

        logger.info("Ingestion Pipeline initialized successfully.")

    def ingest(self, FILE_PATH: str):

        try:
            logger.info(f"Starting ingestion for: {FILE_PATH}")

            # ---------------------------------
            # Load document
            # ---------------------------------

            loader = LoaderFactory.get_loader(
                Path(FILE_PATH)
            )

            documents = loader.load(FILE_PATH)

            logger.info(
                f"Loaded {len(documents)} document(s)."
            )

            # ---------------------------------
            # Chunk document
            # ---------------------------------

            chunks = self.chunker.split_documents(
                documents
            )

            logger.info(
                f"Created {len(chunks)} chunks."
            )

            # ---------------------------------
            # Store into Chroma
            # ---------------------------------

            self.vectorstore.add_documents(chunks)

            logger.info(
                "Documents stored successfully."
            )

            return len(chunks)

        except Exception as e:

            logger.exception(
                f"Ingestion Pipeline failed: {e}"
            )

            raise