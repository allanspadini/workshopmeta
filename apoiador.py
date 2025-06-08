import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import json



"""
Projeto: Analisador Inteligente de Requisições de Cliente e Gerador de Testes
Este projeto foca na eficiência operacional e na qualidade, algo crucial para uma consultoria.

O Problema de Negócio: Um novo projeto na Meta começa com uma requisição do cliente, muitas vezes escrita em linguagem natural e ambígua. A partir dela, analistas precisam criar especificações, e desenvolvedores precisam criar código e testes.

A Solução de IA: Uma ferramenta que recebe um texto de requisição do cliente e:
Analisa e Estrutura: Usa um LLM para extrair os requisitos funcionais, atores envolvidos e dados necessários, retornando uma saída estruturada (ex: JSON).
Gera Código (com Copilot): Usa a saída estruturada como um super-comentário no VS Code para que o GitHub Copilot gere o boilerplate do código (ex: classes Python, assinaturas de função).
Gera Testes Unitários: Usa um segundo LLM (ou uma ferramenta como CodiumAI) para ler o código gerado e criar um conjunto de testes unitários (pytest) que validam os requisitos.
Como se Conecta aos Tópicos do Workshop:
Usa a API do Gemini para análise de texto e geração de código.

"""

def analisar_requisicao(requisicao,llm):
    """
    Analisa a requisição do cliente e extrai requisitos funcionais, atores envolvidos e dados necessários.
    
    Args:
        requisicao (str): Texto da requisição do cliente.
        llm: Instância do modelo de linguagem.

    Returns:
        dict: Requisitos estruturados.
    """
    # Simulação de análise de texto
    
    parser = JsonOutputParser()
    prompt = ChatPromptTemplate.from_template("""
                Você é um analista de requisitos de software.

                Sua tarefa é:
                - Extrair os requisitos funcionais.
                - Identificar os atores envolvidos.
                - Identificar os dados necessários.

                Entrada:
                {requisicao}

                Responda **APENAS com um JSON**, no seguinte formato:

                {format_instructions}
            """)

    #Preparação da cadeia de mensagens
    chain = prompt | llm | parser

    requisitos = chain.invoke({
        "requisicao": requisicao,
        "format_instructions": parser.get_format_instructions()
    })

    return requisitos



def main():
    
    
    st.title("Analisador Inteligente de Requisições")
    st.markdown("""
    Este aplicativo analisa requisições de clientes e extrai:
    - Requisitos funcionais
    - Atores envolvidos 
    - Dados necessários
    """)

    # Carregar a chave de API do Gemini
    load_dotenv()
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-preview-04-17",
        temperature=0.2,
        max_tokens=1000,
        top_p=0.95,
        api_key=GEMINI_API_KEY
    )

    # Input do usuário
    requisicao_cliente = st.text_area(
        "Digite a requisição do cliente:",
        placeholder="Ex: O sistema deve permitir que o usuário crie uma conta, faça login e visualize seu perfil."
    )

    if st.button("Analisar Requisição"):
        if requisicao_cliente:
            with st.spinner("Analisando requisição..."):
                try:
                    requisitos = analisar_requisicao(requisicao_cliente, llm)
                    st.success("Análise concluída!")
                    
                    # Exibir resultados em um formato mais amigável
                    st.subheader("Requisitos Estruturados")
                    st.json(requisitos)
                except Exception as e:
                    st.error(f"Erro ao analisar requisição: {str(e)}")
        else:
            st.warning("Por favor, insira uma requisição para análise.")

if __name__ == "__main__":
    main()
