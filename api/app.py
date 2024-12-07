from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
from langchain_community.llms import Ollama
import uvicorn
import os

from dotenv import load_dotenv

load_dotenv()

#os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain server",
    version="1.0",
    description="A Simple API Server"

)


""""
add_routes(
    app,
    ChatOpenAI(),
    path="/chat-openai"
)


model=ChatOpenAI()
"""


#ollama llama3.2
llm=Ollama(model="llama3.2")

prompt1=ChatPromptTemplate.from_template("write me an essay about {topic} in 100 words")
prompt2=ChatPromptTemplate.from_template("write me a poem about {topic} for a 5 years child with 100 words")


"""
add_routes(
    app,
    prompt1|model,
    path="/essay"
)
"""


add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)