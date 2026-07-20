from backend.core.logger import logger
from backend.retrieval.hybrid_retriever import HybridRetriever
from backend.reranker.reranker import CohereReranker
from backend.llm.llm_factory import LLMFactory
from backend.prompts.prompt_template import RAG_PROMPT


class RAGPipeline:
    """
    End-to-end Retrieval Augmented Generation Pipeline.
    """

    def __init__(self, documents):

        logger.info("Initializing RAG Pipeline...")

        self.retriever = HybridRetriever(documents)
        self.reranker = CohereReranker()
        self.llm = LLMFactory.get_llm()

        logger.info("RAG Pipeline initialized successfully.")

    def ask(self, question: str) -> str:

        try:
            logger.info(f"Received question: {question}")

            # ---------------------------------------
            # Retrieve documents
            # ---------------------------------------
            retrieved_docs = self.retriever.retrieve(question)

            logger.info(
                f"Retrieved {len(retrieved_docs)} documents."
            )

            # ---------------------------------------
            # Rerank documents
            # ---------------------------------------
            reranked_docs = self.reranker.rerank(
                query=question,
                documents=retrieved_docs
            )

            logger.info(
                f"Selected {len(reranked_docs)} reranked documents."
            )

            # ---------------------------------------
            # Build Context
            # ---------------------------------------
            context = "\n\n".join(
                doc.page_content
                for doc in reranked_docs
            )

            # ---------------------------------------
            # Create Prompt
            # ---------------------------------------
            prompt = RAG_PROMPT.invoke(
                {
                    "context": context,
                    "question": question
                }
            )

            logger.info("Prompt generated successfully.")

            # ---------------------------------------
            # Generate Answer
            # ---------------------------------------
            answer = self.llm.generate(
                prompt.to_string()
            )

            logger.info("Answer generated successfully.")

            return answer

        except Exception as e:

            logger.exception(
                f"RAG Pipeline failed: {e}"
            )

            raise