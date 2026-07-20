from dotenv import load_dotenv
from pathlib import Path
import os

# ---------------------------------------------------------
# Project Root Directory
# ---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]

# Load environment variables
load_dotenv(BASE_DIR / ".env")


class Settings:

    # =====================================================
    # Project Information
    # =====================================================
    PROJECT_NAME = "Ask My Docs"

    # =====================================================
    # API Keys
    # =====================================================
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    COHERE_API_KEY = os.getenv("COHERE_API_KEY")
    HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

    # =====================================================
    # LLM & Embedding Models
    # =====================================================
    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "llama-3.1-8b-instant"
    )

    EMBED_MODEL = os.getenv(
        "EMBED_MODEL",
        "embed-english-v3.0"
    )
    EMBEDDING_PROVIDER = "cohere"

    # =====================================================
    # Text Chunking Configuration
    # =====================================================

    # Maximum characters in one chunk
    CHUNK_SIZE = int(
        os.getenv("CHUNK_SIZE", 1000)
    )

    # Characters repeated between chunks
    CHUNK_OVERLAP = int(
        os.getenv("CHUNK_OVERLAP", 200)
    )

    # =====================================================
    # Retriever Configuration
    # =====================================================

    # Number of documents retrieved from ChromaDB
    TOP_K = int(
        os.getenv("TOP_K", 5)
    )

    # =====================================================
    # Vector Database
    # =====================================================

    VECTOR_DB = os.getenv(
    "VECTOR_DB",
    "chroma"
    
    ) 
    
    COLLECTION_NAME = os.getenv(
        "COLLECTION_NAME",
        "ask_my_docs"
    )
    

    # =====================================================
    # Directories
    # =====================================================

    DATA_DIR = BASE_DIR / "data"

    UPLOAD_DIR = BASE_DIR / os.getenv(
        "UPLOAD_DIR",
        "data/uploads"
    )

    CHROMA_DB_PATH = BASE_DIR / os.getenv(
        "CHROMA_DB_PATH",
        "data/chroma_db"
    )

    # =====================================================
    # Create Directories Automatically
    # =====================================================

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    CHROMA_DB_PATH.mkdir(parents=True, exist_ok=True)
    


# Singleton object
settings = Settings()