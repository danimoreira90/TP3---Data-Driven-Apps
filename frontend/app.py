import sys
import os
import streamlit as st

project_root = 'D:\\Pastas\\Infnet\\Infnet - 2024.2\\Desenvolvimento Data-Driven Apps Python\\TP3'
sys.path.append(project_root)

from backend.utils import MEMORY

from backend.main import load_agent

import requests

from langchain_community.callbacks.streamlit import StreamlitCallbackHandler

FASTAPI_BASE_URL = "http://localhost:8000"

def get_energy_data(limit, query):
    # Construindo a URL para fazer a requisição ao FastAPI
    response = requests.get(f"{FASTAPI_BASE_URL}/energy", params={"limit": limit, "query": query})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data")
    
    
def main():
    st.title('Consulta de Consumo de Energia')
    query = st.text_input('Buscar consumo por palavra-chave:', '', key='query_input')
    limit = st.slider('Número de resultados', 1, 100, 5, key='limit_slider')

    if st.button('Buscar', key='search_button'):
        try:
            data = get_energy_data(limit, query)
            if data and 'result' in data and 'records' in data['result']:
                records = data['result']['records']
                if records:
                    st.write('Resultados encontrados:')
                    st.dataframe(records)  # Exibindo os dados em um dataframe
                else:
                    st.write('Nenhum resultado encontrado.')
            else:
                st.write('Nenhum dado disponível para mostrar.')
        except Exception as e:
            st.error(f"Erro ao buscar dados: {str(e)}")


def main():
    st.title('Aplicação de Eficiência Energética')

    # Adicionando uma barra lateral com opções de consulta
    consulta_opcao = st.sidebar.selectbox(
        "Escolha uma opção de consulta:",
        ("Consulta a API da ANEEL", "Consulta ao modelo assistente de eficiência energética")
    )

    # Lógica para lidar com as escolhas na barra lateral
    if consulta_opcao == "Consulta a API da ANEEL":
        # Inclua aqui a lógica para consulta à API da ANEEL
        st.subheader("Consulta a API da ANEEL")
        # Adicione interatividade ou display de dados relacionados à API da ANEEL
    elif consulta_opcao == "Consulta ao modelo assistente de eficiência energética":
        # Inclua aqui a lógica para consulta ao modelo de eficiência energética
        st.subheader("Consulta ao modelo assistente de eficiência energética")
        # Adicione interatividade ou display de dados relacionados ao modelo assistente

if __name__ == "__main__":
    main()



st.title('Energy Efficiency Assistant')
agent = load_agent()

user_input = st.text_input("Ask something about energy efficiency:")
if st.button('Get Answer'):
    response = agent.invoke({"input": user_input})
    st.write(response)

st.header("Ask your question Padawan!")

strategy = st.radio(
    "Reasoning Strategy",
    ("plan-and-solve", "zero-shot-react"),
)

tool_names = st.multiselect(
    "Which tools would you like to use?",
    [
        "critical_search",
        "llm-math",
        "ddg-search",
        "wolfram_alpha",
        "google_search",
        "wikipedia",
        "arxiv",
        "python_repl",
    ],
    ["ddg-search", "wolfram_alpha", "wikipedia"]
)

if st.sidebar.button("Clear message history"):
    MEMORY.chat_memory.clear()
    
avatars = {
    "human": "user",
    "ai": "assistant"
}
for msg in MEMORY.chat_memory.messages:
    st.chat_message(avatars[msg.type]).write(msg.content)
    
agent_chain = load_agent(tool_names=tool_names, strategy=strategy)

if prompt := st.chat_input(placeholder="Ask me anything!!"):
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        response = agent_chain.invoke(
            {"input": prompt} ,
            {"callbacks": [st_callback]}
        )
        st.write(response["output"])