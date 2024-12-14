from langchain.llms import OpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.chains import LLMChain

def load_llm(api_key):
    # Instancia o modelo GPT-4 da OpenAI
    return OpenAI(api_key=api_key, model_name="gpt-4")
