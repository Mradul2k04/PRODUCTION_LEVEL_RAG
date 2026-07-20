from langchain_core.documents import Document
from backend.vectorstore.chroma_store import ChromaStore

store = ChromaStore()

with open("data/uploads/sample.txt", "r", encoding="utf-8") as f:
    text = f.read()

doc = Document(page_content=text)

store.add_documents([doc])

results = store.similarity_search("What is this document about?")

print(results)