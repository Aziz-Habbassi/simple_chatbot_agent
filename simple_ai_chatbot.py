from langchain_ollama import OllamaLLM

llm=OllamaLLM(model="llama3.1:8b")

print("Welcome to the AI Chatbot!")

while True:
    question=input("Your question or 'exit' to end the conversation:\n")
    if question.lower()=="exit":
        print("Have a nice Day , GoodBye !")
        break
    response = llm.invoke(question)
    print("\n AI : "+response)