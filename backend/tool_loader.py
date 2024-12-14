from langchain.tools import Tool

def load_tools():
    # Aqui você pode definir ferramentas específicas, como APIs de eficiência energética
    return [
        Tool(name="example_tool", func=lambda x: "Response from tool")
    ]