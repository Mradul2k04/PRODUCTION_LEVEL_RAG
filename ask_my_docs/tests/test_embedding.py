from backend.embeddings.embedding_model import CohereEmbedding


def test_embedding():
    embedding = CohereEmbedding()

    with open("data/uploads/sample.txt", "r", encoding="utf-8") as file:
        text = file.read()

    doc_embedding = embedding.embed_documents([text])
    query_embedding = embedding.embed_query("What is this document about?")

    print("Document Embedding Generated:", len(doc_embedding))
    print("Query Embedding Dimension:", len(query_embedding))

    print("✅ Embedding test passed!")


if __name__ == "__main__":
    test_embedding()