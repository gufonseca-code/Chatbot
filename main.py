from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model='llama3.2:1b')
result = model.invoke(input='Como você está?')
print(result)