import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate #This will tell my LLM how to behave
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
#LangSmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

#Prompt Templaye
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)
#streamlit framework
st.title("LangChain Demo with Llama3")
input_text=st.text_input("How can I help you?")

#Ollama Llama3 model
llm=Ollama(model='llama3')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text: #what to do after i enter input text and press enter
    response=chain.invoke({"question":input_text}) #my input text is my question
    st.write(response)
