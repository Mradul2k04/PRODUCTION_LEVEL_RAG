from backend.services.ingest_pipeline import IngestionPipeline

pipeline = IngestionPipeline()

num_chunks = pipeline.ingest(
    "data/uploads/sample.txt"
)

print(f"Stored {num_chunks} chunks.")