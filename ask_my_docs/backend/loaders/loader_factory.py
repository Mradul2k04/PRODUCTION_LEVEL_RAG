
from pathlib import Path
from backend.loaders.base_loader import BaseLoader

from backend.loaders.pdf_loader import PDFLoader
from backend.loaders.docx_loader import DOCXLoader
from backend.loaders.txt_loader import TXTLoader
from backend.core.logger import logger


class LoaderFactory:

    @staticmethod
    def get_loader(FILE_PATH: str) -> BaseLoader:
        """
        Returns the appropriate loader object based
        on the file extension.

        Parameters
        ----------
        file_path : str
            Path of the uploaded file.

        Returns
        -------
        BaseLoader
            Instance of PDFLoader, DOCXLoader or TXTLoader.

        Raises
        ------
        ValueError
            If the file extension is not supported.
        """

        # Extract extension
        extension = Path(FILE_PATH).suffix.lower()

        logger.info(f"Detecting loader for file type: {extension}")

        # -------------------------------
        # PDF
        # -------------------------------
        if extension == ".pdf":
            logger.info("Using PDFLoader")
            return PDFLoader()

        # -------------------------------
        # DOCX
        # -------------------------------
        elif extension == ".docx":
            logger.info("Using DOCXLoader")
            return DOCXLoader()

        # -------------------------------
        # TXT
        # -------------------------------
        elif extension == ".txt":
            logger.info("Using TXTLoader")
            return TXTLoader()

        # -------------------------------
        # Unsupported
        # -------------------------------
        else:

            logger.error(f"Unsupported file type: {extension}")

            raise ValueError(
                f"Unsupported file format: {extension}"
            )
            
            
            
"""
loader_factory.py

Purpose
-------
This module implements the Factory Design Pattern.

Instead of creating PDFLoader(), DOCXLoader(), or TXTLoader()
throughout the project, we ask the factory to create the correct
loader based on the uploaded file type.

Benefits
--------
1. Cleaner code
2. Easy to extend
3. Follows Open/Closed Principle (SOLID)
4. Single place to manage supported file types
"""            