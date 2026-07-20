from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

from backend.core.logger import logger
from backend.loaders.base_loader import BaseLoader

class TXTLoader(BaseLoader):
    
    
    def load(self, FILE_PATH: str) -> list[Document]:

        logger.info(f"Loading TXT File: {FILE_PATH}")
        
        try:

            loader = TextLoader(
                file_path=FILE_PATH,
                encoding="utf-8"
            )

            documents = loader.load()

            logger.info(f"Loaded {len(documents)} document(s).")

            return documents

        except Exception as e:

            logger.exception(f"Failed to load TXT: {e}")

            raise
