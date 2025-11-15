from langchain_ollama import OllamaLLM
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
import streamlit as st


llm=OllamaLLM(model="llama3.1:8b")# or choose the model you want

if "chat_history" not in st.session_state :
    st.session_state.chat_history=ChatMessageHistory()
prompt=PromptTemplate(input_variables=["chat_history","question"],template="Previous conversation: {chat_history}\nUser: {question}\nAI:")

def run_chain(question):
    chat_history_text="\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in st.session_state.chat_history.messages])

    response = llm.invoke(prompt.format(chat_history=chat_history_text,question=question))

    st.session_state.chat_history.add_user_message(question)
    st.session_state.chat_history.add_ai_message(response)

    return response

st.title("🤖 Welcome to the AI Chatbot!")
st.write("Ask me Anythin , if you want to quit just enter 'exit' to end the conversation")


question=st.text_input("Your Question : ")
if question.lower()=="exit":
    st.write("🤖 Have a nice Day , GoodBye !")

response = run_chain(question=question)
st.write("You : "+question)
st.write("🤖 AI : "+response)

st.subheader("📜Chat History")
for msg in st.session_state.chat_history.messages:
    st.write(msg.type.capitalize()+" : "+msg.content)