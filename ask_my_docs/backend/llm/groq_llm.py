from langchain_groq import ChatGroq
from backend.core.config import settings
from backend.core.logger import logger
from backend.llm.base_llm import BaseLLM

class GroqLLM(BaseLLM):
    """
    Groq LLM implementation.
    """
    def __init__(self):
        try:
            logger.info("Initializing Groq LLM..")
            
            self.llm=ChatGroq(
                model=settings.MODEL_NAME,
                temperature=0
            )
            
            logger.info("Groq LLM initialized successfully.")
            
        except Exception as e:
            logger.exception(f"Failed to initialize Groq LLM: {e}")
            raise
        
    def generate(self,prompt :str)->str:
        try:
            logger.info("Generating response from Groq...")
            
            response=self.llm.invoke(prompt)
            
            logger.info("Respnse generated Successfully")
            
            return response.content
        except Exception as e:
            logger.exception(f"Error while generating response : {e}")
            raise