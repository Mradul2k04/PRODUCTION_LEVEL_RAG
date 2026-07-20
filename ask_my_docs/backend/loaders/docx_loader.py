from langchain_community.document_loaders import Docx2txtLoader
from langchain_core.documents import Document

from backend.loaders.base_loader import BaseLoader
from backend.core.logger import logger

class DOCXLoader(BaseLoader):
    
    def load(self, FILE_PATH:str) ->list[Document]:
        logger.info(f"Loding DOCX {FILE_PATH}")
        
        try:
            loader=Docx2txtLoader(FILE_PATH)
            
            documents=loader.load()
            
            logger.info(f"Loaded {len(documents)} document(s).")
            
            return documents
        
        except Exception as e:
            
            logger.exception(f"Failed to load DOCX: {e}")
             
            raise 