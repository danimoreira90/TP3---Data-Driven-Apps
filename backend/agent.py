from langchain.llms import OpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.chains import LLMChain
import os


def load_llm(api_key):
    return OpenAI(api_key=os.getenv('OPENAI_API_KEY'), model_name="gpt-4")
