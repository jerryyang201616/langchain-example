from dotenv import load_dotenv
import os
import asyncio

from langchain_openai import ChatOpenAI

# Load .env
load_dotenv()
deepseek_key = os.getenv("DEEPSEEK_API_KEY")

llm = ChatOpenAI(
    api_key=deepseek_key,
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
)

async def async_stream():
    chunks = []
    async for chunk in llm.astream("hello"):
        chunks.append(chunk)
        print(chunk.content, end="", flush=True)

    print("\n\n--- All Chunks Collected ---")
    print(chunks)


# Jupyter-safe execution
try:
    asyncio.get_running_loop()
    await async_stream()
except RuntimeError:
    asyncio.run(async_stream())
