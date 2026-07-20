
# Import Loader Factory
from backend.loaders.loader_factory import LoaderFactory

# Import Logger
from backend.core.logger import logger


def test_loader_factory():
    """
    Test the Loader Factory.
    """

    # ---------------------------------------------------------
    # Replace with your document path
    # ---------------------------------------------------------
    file_path = "data/uploads/sample.txt"

    logger.info("=" * 60)
    logger.info("Starting Loader Factory Test")
    logger.info("=" * 60)

    try:

        # -----------------------------------------------------
        # Step 1 : Factory decides which loader to use
        # -----------------------------------------------------
        loader = LoaderFactory.get_loader(file_path)

        logger.info(f"Loader Selected : {loader.__class__.__name__}")

        # -----------------------------------------------------
        # Step 2 : Load the document
        # -----------------------------------------------------
        documents = loader.load(file_path)

        logger.info(f"Total Documents Loaded : {len(documents)}")

        print("\n" + "=" * 60)
        print("LOADER FACTORY TEST SUCCESSFUL")
        print("=" * 60)

        print(f"\nSelected Loader : {loader.__class__.__name__}")

        print(f"Total Documents : {len(documents)}")

        # -----------------------------------------------------
        # Display First Document
        # -----------------------------------------------------
        if documents:

            first_doc = documents[0]

            print("\nFirst Document Metadata")
            print("-" * 60)
            print(first_doc.metadata)

            print("\nFirst Document Content")
            print("-" * 60)
            print(first_doc.page_content[:500])

        print("\n" + "=" * 60)

    except Exception as e:

        logger.exception(f"Loader Factory Test Failed : {e}")

        print("\nTest Failed!")
        print(e)


if __name__ == "__main__":
    test_loader_factory()