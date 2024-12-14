from fastapi import FastAPI
from .dependencies.data_manager import fetch_energy_data
from dotenv import load_dotenv
import os
from langchain_community.llms import OpenAI
from langchain.agents import create_react_agent
from langchain.chains import LLMChain
from backend.tool_loader import load_tools


load_dotenv()

app = FastAPI()

@app.get("/energy")
async def get_energy_data(limit: int = 5, query: str = ""):
    data = fetch_energy_data(limit, query)
    return data



def load_agent():
    llm = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), model_name="gpt-4")
    tools = load_tools()
    agent = create_react_agent(llm=llm, tools=tools)
    return LLMChain(agent)

if __name__ == "__main__":
    agent = load_agent()
    print("Agent loaded successfully!")