from backend.llm.llm_factory import LLMFactory


llm = LLMFactory.get_llm()

response = llm.generate(
    "Explain Retrieval Augmented Generation in two lines."
)

print(response)