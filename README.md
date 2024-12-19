
# Assistente de Eficiência Energética

## Descrição

Este projeto desenvolve um assistente interativo focado na eficiência energética, utilizando uma combinação de modelos de linguagem de última geração e APIs especializadas. O objetivo é fornecer um recurso acessível e informativo para indivíduos e organizações interessadas em melhorar a eficiência energética e promover práticas sustentáveis.

## Funcionalidades

- **Consulta à API da ANEEL**: Acesso direto a dados e informações regulatórias sobre o setor energético brasileiro, permitindo consultas detalhadas sobre normativas, geração de energia e mais.
- **Assistente de Eficiência Energética**: Utilizando um modelo de linguagem avançado, o assistente pode fornecer respostas detalhadas sobre questões de eficiência energética, desde dicas para reduzir o consumo até análises complexas de tendências de energia.
- **Recomendações Personalizadas**: Baseado em inputs do usuário, o sistema oferece recomendações personalizadas para melhorar a eficiência energética em diferentes cenários.

## Tecnologias Utilizadas

- **Streamlit**: Para uma interface interativa que permite aos usuários interagir com o assistente e visualizar dados.
- **FastAPI**: Usado para criar uma API robusta que serve dados energéticos e lida com as solicitações do usuário.
- **LangChain e OpenAI**: Combinação de tecnologias para processamento de linguagem natural, proporcionando uma interação natural e baseada em conhecimento atualizado sobre eficiência energética.

## Como Usar

Para iniciar o assistente, siga os passos abaixo:

1. Instale as dependências usando `pip install -r requirements.txt`.
2. Execute o servidor FastAPI com `uvicorn backend.main:app --reload`.
3. Abra o aplicativo Streamlit com `streamlit run frontend/app.py`.

A interface do Streamlit permitirá que você escolha entre consultar diretamente a API da ANEEL ou interagir com o assistente de eficiência energética.

