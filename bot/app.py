from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHIAN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHIAN_TRACING_V2"]=os.getenv("LANGCHAIN_TRACING_V2")

#Prompt Template

prompt_template=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpfl assistant,please repond to the user queries"),
        ("user","Question:{question}")
    ]
)

#streamlit framework

st.title("Langchain Demo With OpenAI API")
input_text=st.text_input("Search the topic u want")

#openAI LLM
llm=ChatOpenAI(model="",temperature=0.7)
output_parser=StrOutputParser()
chain=prompt_template|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))