import requests
import streamlit as st

def get_ollama_response(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",
                           json={'input':{'topic':input_text}})
    
    return response.json()['output']

st.title('Langchain Demo With Llama3.2 API')
input_text1=st.text_input("Write a poem on")

if input_text1:
    st.write(get_ollama_response(input_text1))