
import base64
import streamlit as st
from pathlib import Path
from backend.services.ingest_pipeline import IngestionPipeline
from backend.services.rag_pipeline import RAGPipeline
from langchain_core.documents import Document


st.set_page_config(
    page_title="Ask My Docs",
    page_icon="📄",
    layout="wide"
)

# ------------------------------------
# Background Image
# ------------------------------------

def get_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()


image_path = Path(__file__).parent / "assets" / "rag_cyber_background.png"

img = get_base64(image_path)

st.markdown(
    f"""
<style>

.stApp {{
    background:
        linear-gradient(
            rgba(255,255,255,0.15),
            rgba(255,255,255,0.15)
        ),
        url("data:image/png;base64,{img}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* Main container */
.main > div {{
    background-color: rgba(255,255,255,0.20);
    border-radius: 10px;
    padding: 10px;
}}

/* Title */
h1 {{
    color: #ffffff;
    text-align: center;
}}

/* Text */
p, label {{
    color: white !important;
    font-size: 15px;
}}

</style>
""",
  unsafe_allow_html=True
)


# ------------------------------------
# Title
# ------------------------------------

st.title("📄 Ask My Docs")
st.write("Upload your documents and ask questions.")

# ------------------------------------
# Session State
# ------------------------------------

if "pipeline" not in st.session_state:
    st.session_state.pipeline = None

# ------------------------------------
# File Upload
# ------------------------------------

uploaded_file = st.file_uploader(
    "Upload PDF / DOCX / TXT",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:

    save_path = f"data/uploads/{uploaded_file.name}"

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully.")

    with st.spinner("Processing document..."):

        ingestion = IngestionPipeline()

        ingestion.ingest(save_path)

    st.success("Document indexed successfully.")

    from backend.loaders.loader_factory import LoaderFactory
    from backend.chunking.chunker import DocumentChunker

    loader = LoaderFactory.get_loader(save_path)

    docs = loader.load(save_path)

    chunker = DocumentChunker()

    chunks = chunker.split_documents(docs)

    st.session_state.pipeline = RAGPipeline(chunks)

# ------------------------------------
# Chat
# ------------------------------------

question = st.text_input(
    "Ask your question"
)

if st.button("Ask"):

    if st.session_state.pipeline is None:

        st.warning("Upload a document first.")

    else:

        with st.spinner("Thinking..."):

            answer = st.session_state.pipeline.ask(
                question
            )

        st.markdown("### Answer")

        st.write(answer)