from fastapi import FastAPI
from .dependencies.data_manager import fetch_energy_data
from dotenv import load_dotenv
import os
from langchain_community.llms import OpenAI
from langchain.agents import create_react_agent
from langchain.chains import LLMChain
from backend.tool_loader import load_tools
from langchain_core.prompts import PromptTemplate



load_dotenv()

app = FastAPI()

@app.get("/energy")
async def get_energy_data(limit: int = 5, query: str = ""):
    data = fetch_energy_data(limit, query)
    return data



def load_agent():
    llm = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), model_name="gpt-4")
    tool_names = ['ddg-search', 'wolfram_alpha', 'google_search', 'wikipedia', 'arxiv', 'python_repl', 'critical_search']
    tools = load_tools(tool_names, llm=llm)
    
    # Define um prompt complexo com base na documentação
    template = '''
    Answer the following questions as best you can. You have access to the following tools:
    
    {tools}
    
    Use the following format:
    
    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question
    
    Begin!
    
    Question: {input}
    Thought:{agent_scratchpad}
    '''
    prompt = PromptTemplate.from_template(template, tool_names=tool_names, tools=tools)
    
    # Cria o agente com o prompt complexo
    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
    
    return LLMChain(agent)

if __name__ == "__main__":
    agent = load_agent()
    print("Agent loaded successfully!")