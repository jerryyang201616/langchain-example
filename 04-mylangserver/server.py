# server.py
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langserve import add_routes

from chain import create_chain

# Load environment variables
load_dotenv()

app = FastAPI(
    title="DeepSeek LangServe API",
    description="Serve DeepSeek LLM using LangChain + LangServe",
    version="1.0.0",
)

# Add DeepSeek chain under /deepseek
add_routes(
    app,
    create_chain(),
    path="/deepseek"
)

@app.get("/")
def root():
    return {"message": "DeepSeek LangServe is running!"}
