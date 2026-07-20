from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from backend.core.logger import logger
from langchain_core.documents import Document
from backend.loaders.base_loader import BaseLoader

class PDFLoader(BaseLoader):
    """
    PDF Loader Class
    
    """
    def load(self, FILE_PATH:str) -> list[Document]:
        
        logger.info(f"Loading PDF : {FILE_PATH}")
        try:
            loader=PyPDFLoader(FILE_PATH)
            
            documents=loader.load()
            
            logger.info(f"Loaded {len(documents)}pages.")
            
            return documents
        except Exception as e:
            logger.exception(f"Failed tp load PDF :{e}")
            
            raise 