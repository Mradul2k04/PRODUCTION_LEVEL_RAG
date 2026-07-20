from backend.loaders.pdf_loader import PDFLoader
from backend.core.logger import logger

def test_pdf_loader():
    
    pdf_path=r"data\uploads\Project_ Production-Ready RAG Application.pdf"
    
    logger.info("Starting PDF Loader Test...")
    
    # Create Loader Object
    loader = PDFLoader()
    
    # Load PDF
    documents = loader.load(pdf_path)

    logger.info(f"Total Pages Loaded : {len(documents)}")

    print("\n==============================")
    print("PDF LOADED SUCCESSFULLY")
    print("==============================\n")

    print(f"Total Pages : {len(documents)}")

    # ------------------------------------------------------------
    # Display First Page
    # ------------------------------------------------------------
    if documents:

        print("\nFirst Page Content:\n")
        print(documents[0].page_content[:500])

        print("\nMetadata:\n")
        print(documents[0].metadata)


if __name__ == "__main__":
    test_pdf_loader()