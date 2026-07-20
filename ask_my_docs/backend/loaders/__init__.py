"""
Loaders Package

Exports all available document loaders.
"""

from .pdf_loader import PDFLoader
from .docx_loader import DOCXLoader
from .txt_loader import TXTLoader

__all__ = [
    "PDFLoader",
    "DOCXLoader",
    "TXTLoader",
]