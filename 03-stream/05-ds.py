import os
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load API key from .env
load_dotenv()
deepseek_key = os.getenv("DEEPSEEK_API_KEY")

if deepseek_key is None:
    raise ValueError("DEEPSEEK_API_KEY not found in .env")

# DeepSeek LLM config
def get_llm():
    return ChatOpenAI(
        api_key=deepseek_key,
        base_url="https://api.deepseek.com",
        model="deepseek-chat",
    )


async def task1():
    llm = get_llm()
    chunks = []

    async for chunk in llm.astream("天空是什么颜色？"):
        chunks.append(chunk)
        if len(chunks) == 2:
            print("\n第二个chunk对象：", chunks[1])

        print(chunk.content or "", end="|", flush=True)


async def task2():
    llm = get_llm()
    chunks = []

    async for chunk in llm.astream("讲个笑话？"):
        chunks.append(chunk)
        if len(chunks) == 2:
            print("\n第二个chunk对象：", chunks[1])

        print(chunk.content or "", end="|", flush=True)


async def main():
    # 顺序执行
    await task1()
    print("\n------ task1 done ------\n")
    await task2()

    # 并发执行（可选）
    # await asyncio.gather(task1(), task2())


# For Jupyter compatibility:
try:
    asyncio.get_running_loop()
    await main()
except RuntimeError:
    asyncio.run(main())
