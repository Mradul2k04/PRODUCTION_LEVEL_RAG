from langchain_chroma import Chroma
from backend.core.logger import logger
from backend.core.config import settings
from backend.embeddings.embedding_model import CohereEmbedding
from backend.vectorstore.base_vectorestore import BaseVectorStore

class ChromaStore(BaseVectorStore):
     """
    Chroma Vector Store Implementation.
    """
     def __init__(self):
          logger.info("Initializing Chroma Vector Store...")
          
          embedding=CohereEmbedding()
          
          self.vectorstore=Chroma(
              collection_name=settings.COLLECTION_NAME,
              persist_directory=str(settings.CHROMA_DB_PATH),
              embedding_function=embedding.embedding,
          )
          
          logger.info("Chroma Vector Store initialized successfully.")
          
     def add_documents(self, documents):
        try:
            logger.info(f"Adding {len(documents)} documents to Chroma.")
            self.vectorstore.add_documents(documents)
            logger.info("Documents added successfully.")

        except Exception as e:
            logger.exception(f"Error adding documents: {e}")
            raise
        
     def similarity_search(self, query, k=None):
        try:
            logger.info("Performing similarity search.")

            return self.vectorstore.similarity_search(
                query=query,
                k=k or settings.TOP_K
            )
        except Exception as e:
            logger.exception(f"Similarity search failed: {e}")
            raise
        
     def similarity_search_with_score(self, query, k=None):
        try:
            logger.info("Performing similarity search with score.")

            return self.vectorstore.similarity_search_with_score(
                query=query,
                k=k or settings.TOP_K
            )

        except Exception as e:
            logger.exception(f"Similarity search with score failed: {e}")
            raise
        
     def get_all_documents(self):
        try:
            logger.info("Fetching all documents from Chroma.")

            data = self.vectorstore.get()

            documents = []

            for text, metadata in zip(
                data["documents"],
                data["metadatas"]
            ):
                from langchain_core.documents import Document

                documents.append(
                    Document(
                        page_content=text,
                        metadata=metadata
                    )
                )

            return documents

        except Exception as e:
            logger.exception(f"Failed to fetch documents: {e}")
            raise

     def clear(self):
        try:
            logger.info("Clearing Chroma collection.")

            self.vectorstore.reset_collection()

            logger.info("Collection cleared successfully.")

        except Exception as e:
            logger.exception(f"Failed to clear collection: {e}")
            raise   
