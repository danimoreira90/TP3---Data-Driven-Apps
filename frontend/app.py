import streamlit as st
import requests

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

if __name__ == "__main__":
    main()

from backend.main import load_agent

st.title('Energy Efficiency Assistant')
agent = load_agent()

user_input = st.text_input("Ask something about energy efficiency:")
if st.button('Get Answer'):
    response = agent.invoke({"input": user_input})
    st.write(response)