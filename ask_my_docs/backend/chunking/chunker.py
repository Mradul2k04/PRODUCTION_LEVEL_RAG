from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from backend.core.config import settings
from backend.core.logger import logger

class DocumentChunker:
   
    def __init__(self):
       
        logger.info("Initializing Document Chunker...")

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            keep_separator=True,
             separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

        logger.info(
            f"Chunker Initialized | "
            f"Chunk Size={settings.CHUNK_SIZE} | "
            f"Overlap={settings.CHUNK_OVERLAP}"
        )

    def split_documents(
        self,
        documents: list[Document]
    ) -> list[Document]:
       
        logger.info(
            f"Received {len(documents)} document(s) for chunking."
        )

        try:
            # Split documents into chunks
            chunks = self.splitter.split_documents(documents)

            logger.info(
                f"Successfully created {len(chunks)} chunks."
            )
            return chunks

        except Exception as e:
            logger.exception(
                f"Failed to split documents: {e}"
            )
            raise