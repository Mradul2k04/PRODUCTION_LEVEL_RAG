from abc import ABC, abstractmethod
# LangChain Document object
from langchain_core.documents import Document

class BaseLoader(ABC):
     """
    Abstract base class for all document loaders.

    Every loader (PDF, DOCX, TXT) must implement the `load()` method.
    """
     @abstractmethod
     def load(self,FILE_PATH:str):
        """
        Load a document and return LangChain Document objects.

        Parameters
        ----------
        file_path : str
            Path to the document.

        Returns
        -------
        list[Document]
            List of LangChain Document objects.

        Raises
        ------
        NotImplementedError
            If a child class does not implement this method.
        """
        pass