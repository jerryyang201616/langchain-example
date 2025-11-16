pip install langserve pip install "langserve[all]"

pip install "langserve[all]" langchain-openai python-dotenv

verify: python -c "import langserve; print(langserve.version)"

server.py from fastapi import FastAPI from langserve import add_routes from langchain_openai import ChatOpenAI

app = FastAPI()

model = ChatOpenAI( model="deepseek-chat", api_key="your_key", base_url="https://api.deepseek.com" )

add_routes(app, model, path="/deepseek")

run: uvicorn server:app --reload --port 8000

call local API: POST http://localhost:8000/deepseek/invoke { "input": "讲个笑话" }


Below is a complete, production-ready LangServe + DeepSeek API server, with:

✅ LangServe
✅ DeepSeek (OpenAI-compatible API)
✅ Streaming endpoint
✅ /invoke synchronous endpoint
✅ /stream streaming endpoint
✅ .env API key loading
✅ FastAPI + Uvicorn
✅ Modern LangChain 0.2+ syntax
✅ Works on Linux / Mac / Windows

You can run this locally and expose your own DeepSeek-powered API.

🚀 1. Install dependencies
pip install "langserve[all]" langchain-openai python-dotenv

📁 2. Project Structure
deepseek_langserve/
│
├── server.py
├── chain.py
└── .env

🧩 3. .env file

Create .env:

DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx

🔗 4. chain.py

Your LangChain chain definition.

# chain.py
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os

def create_chain():
    """Build the DeepSeek chain"""

    model = ChatOpenAI(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com",
        model="deepseek-chat",     # or deepseek-reasoner
        temperature=0.3,
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个专业AI助手，回答要准确简洁。"),
        ("user", "{input}")
    ])

    chain = prompt | model
    return chain

🖥️ 5. server.py

Your LangServe FastAPI server.

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

▶️ 6. Start the server
uvicorn server:app --reload --port 8000

🌐 7. Test the API
🟦 A. Synchronous /invoke endpoint

POST:

http://localhost:8000/deepseek/invoke


Body:

{
  "input": "解释一下为什么天空是蓝色的？"
}


Response:

{
  "output": "天空呈蓝色是因为瑞利散射..."
}

🟩 B. Streaming endpoint

POST:

http://localhost:8000/deepseek/stream


Body:

{
  "input": "写一个50字的故事"
}


You will receive streaming chunks.

🟧 C. Web UI (Swagger)

Open:

http://localhost:8000/docs


You will see:

/deepseek/invoke

/deepseek/stream

/deepseek/batch

All generated automatically by LangServe.

⚡ BONUS: Client Example (Python)
import requests

resp = requests.post(
    "http://localhost:8000/deepseek/invoke",
    json={"input": "讲一个笑话"}
)

print(resp.json())

✔ You now have a full local DeepSeek LLM API server!

This setup lets you:

Build your own OpenAI-like API powered by DeepSeek

Integrate with external tools

Deploy to cloud (Docker instructions available)

Use structured chains, RAG pipelines, tools, async, etc.
