from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the following question:

The context: {context}

The question: {question}

Answer:
"""

model = OllamaLLM(model="llama3.2:1b")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def conversation():
    context = """
    You're a salesman from a clothes store called "My precious" 
    Today is Black Friday and all clothes are 30% off.
    In your store they sell only t-shirts.
    """

    print("Welcome to our store, how may I help you? Type 'quit' to leave our store.")
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            break

        result = chain.invoke({"context": context, "question": user_input})
        print(f"> Salesman: {result}")
        context += f"\nCostumer: {user_input}\nSalesman: {result}"

if __name__ == '__main__':
    conversation()
