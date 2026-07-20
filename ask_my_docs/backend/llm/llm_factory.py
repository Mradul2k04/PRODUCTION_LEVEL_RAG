from backend.llm.groq_llm import GroqLLM
from backend.core.config import settings

class LLMFactory:
    """
    Factory class for LLM providers.
    """
    
    @staticmethod
    def get_llm():
        
        if settings.MODEL_NAME:
            return GroqLLM()
        
        raise ValueError("Unsupported LLM Provider")