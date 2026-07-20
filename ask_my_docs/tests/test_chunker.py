from backend.loaders.loader_factory import LoaderFactory
from backend.chunking.chunker import DocumentChunker
from backend.core.logger import logger


def test_chunker():

    file_path = "data/uploads/sample.txt"

    logger.info("Starting Chunker Test")

    # Load document
    loader = LoaderFactory.get_loader(file_path)
    documents = loader.load(file_path)

    # Chunk document
    chunker = DocumentChunker()
    chunks = chunker.split_documents(documents)

    print(f"\nOriginal Documents : {len(documents)}")
    print(f"Total Chunks       : {len(chunks)}")

    print("\nFirst Chunk:\n")
    print(chunks[0].page_content)

    print("\nMetadata:\n")
    print(chunks[0].metadata)


if __name__ == "__main__":
    test_chunker()