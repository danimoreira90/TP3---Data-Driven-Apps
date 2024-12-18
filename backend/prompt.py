from langchain_core.prompts import PromptTemplate

template = """
Assistant is designed to help with energy efficiency queries.

Assistant has access to the following tools:
{tools}

To use a tool, please use the following format:

Thought: Consider if a tool is needed. If yes:
Action: [Tool Name]
Action Input: [Input necessary for the action]
Observation: [Result of the action]

If no tool is needed:
Thought: I do not need to use a tool.
Final Answer: [Your direct answer]

Question: {input}
"""

prompt = PromptTemplate.from_template(template)
