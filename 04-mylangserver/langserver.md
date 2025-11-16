pip install langserve pip install "langserve[all]"

pip install "langserve[all]" langchain-openai python-dotenv

verify: python -c "import langserve; print(langserve.version)"

server.py from fastapi import FastAPI from langserve import add_routes from langchain_openai import ChatOpenAI

app = FastAPI()

model = ChatOpenAI( model="deepseek-chat", api_key="your_key", base_url="https://api.deepseek.com" )

add_routes(app, model, path="/deepseek")

run: uvicorn server:app --reload --port 8000

call local API: POST http://localhost:8000/deepseek/invoke { "input": "讲个笑话" }
