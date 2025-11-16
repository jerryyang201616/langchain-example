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
