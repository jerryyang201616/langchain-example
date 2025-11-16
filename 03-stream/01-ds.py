from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

# 1. Load API key from .env
load_dotenv()

deepseek_key = os.getenv("DEEPSEEK_API_KEY")
if deepseek_key is None:
    raise ValueError("❌ ERROR: DEEPSEEK_API_KEY not found in .env")

# 2. Create DeepSeek LLM client
llm = ChatOpenAI(
    api_key=deepseek_key,
    base_url="https://api.deepseek.com",
    model="deepseek-chat",     # 或 deepseek-reasoner
)

# 3. Streaming output
chunks = []
for chunk in llm.stream("天空为什么是蓝色的？"):
    chunks.append(chunk)
    print(chunk.content, end="", flush=True)    # no "|"

print("\n--- Streaming Done ---")
