#Deploying Langchain application as REST API with help of LangServe
#LangServe is integrated with FAST API
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes #helps creates API's
from dotenv import load_dotenv
load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")
model=ChatGroq(model="llama-3.3-70b-versatile",groq_api_key=groq_api_key)

#Prompt template
system_template="Translate the following into {language}:"
prompt_template=ChatPromptTemplate.from_messages([
    ('system',system_template),
    ('user',"{text}")
])

parser=StrOutputParser()

#create chain
chain=prompt_template|model|parser

#App Definition----> FastApi is like flask but with added functionality
app=FastAPI(title="Lanchain Server",
            version="1.0",
            description="A simple API server using Langchain runnable interfaces")
##Adding chain routes
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__=="__main__":
    import uvicorn #uvicorn is used for execution of FAST API
    uvicorn.run(app,host="127.0.0.1",port=8000)

#After execution I will get a blank page, do /docs to see results
#out of this i can also try the other parameters present like add /chain/config
#We can also use postman--->helps interact with API's

