from langchain.tools import Tool

def load_tools():
    # Aqui você pode definir ferramentas específicas, como APIs de eficiência energética
    return [
        Tool(name="example_tool", func=lambda x: "Response from tool")
    ]

# tool_loader.py
from langchain.agents import AgentExecutor, Tool, create_self_ask_with_search_agent
from langchain.chains import LLMMathChain
from langchain_community.tools import (
    ArxivQueryRun, WikipediaQueryRun, WolframAlphaQueryRun, GoogleSearchRun, DuckDuckGoSearchRun
)
from langchain_community.utilities import (
    ArxivAPIWrapper, WikipediaAPIWrapper, WolframAlphaAPIWrapper, GoogleSearchAPIWrapper, DuckDuckGoSearchAPIWrapper
)
from langchain_core.language_models import BaseLanguageModel
from langchain_core.tools import BaseTool
from langchain_experimental.tools import PythonREPLTool
from langchain import hub
from typing import Optional

# Cria uma instância da ferramenta REPL de Python para execução de comandos Python
python_repl = PythonREPLTool()

def load_tools(tool_names: list[str], llm: Optional[BaseLanguageModel] = None) -> list[BaseTool]:
    # Puxa um prompt específico do Hub de LangChain
    prompt = hub.pull("hwchase17/self-ask-with-search")
    
    # Configura as ferramentas de busca com seus respectivos wrappers
    available_tools = {
        "ddg-search": DuckDuckGoSearchRun(api_wrapper=DuckDuckGoSearchAPIWrapper()),
        "wolfram_alpha": WolframAlphaQueryRun(api_wrapper=WolframAlphaAPIWrapper()),
        "google_search": GoogleSearchRun(api_wrapper=GoogleSearchAPIWrapper()),
        "wikipedia": WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper()),
        "arxiv": ArxivQueryRun(api_wrapper=ArxivAPIWrapper()),
        "python_repl": Tool(
            name="python_repl",
            description="Execute Python commands.",
            func=python_repl.run
        ),
        "critical_search": Tool.from_function(
            func=lambda query: "Response for query: " + query,
            name="Self-ask agent",
            description="Answers complex questions."
        )
    }
    
    # Retorna apenas as ferramentas especificadas na lista de entrada
    return [available_tools[name] for name in tool_names if name in available_tools]
