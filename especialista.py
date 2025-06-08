




"""
Projeto 1: Chatbot Especialista em Documentação Técnica (RAG)
Este projeto é o ponto de partida ideal. É visualmente impactante, resolve uma dor real de qualquer desenvolvedor e é a introdução perfeita ao conceito de LLMs aplicados.

O Problema de Negócio: Desenvolvedores da Meta perdem tempo precioso navegando por documentações extensas e complexas da SAP, Microsoft ou de projetos legados para encontrar respostas específicas.

A Solução de IA: Um chatbot que responde a perguntas em linguagem natural ("Como faço para criar uma fatura no S/4HANA usando a BAPI X?") com base em uma coleção privada de documentos (PDFs, manuais, etc.). Utiliza a técnica de Retrieval-Augmented Generation (RAG).

Como se Conecta aos Tópicos do Workshop:

Construção de prompts inteligentes: O sistema inteiro depende de um prompt que instrui o LLM a responder usando apenas o contexto fornecido.
Exploração de LLMs multimodais: A base de conhecimento pode incluir diagramas e tabelas, e você pode discutir como modelos multimodais poderiam interpretar essas imagens.
Construção de chat especialista: É a definição literal deste tópico.
Desenvolvimento com apoio de IAs Generativas: O código para o chatbot pode ser acelerado drasticamente usando o GitHub Copilot.
Stack de Tecnologia Sugerido (Python):

Orquestração de LLM: LangChain ou LlamaIndex para gerenciar o fluxo de RAG (carregar docs, criar embeddings, consultar).
Modelos: Pode usar a API da OpenAI (GPT-4) para alta qualidade ou um modelo open-source como Llama 3 via Ollama para rodar localmente.
Vector Store: ChromaDB ou FAISS para armazenar os vetores da documentação. É simples e roda em memória/localmente.
Interface Gráfica: Streamlit para criar a interface de chat de forma rápida e interativa.
Nível de Complexidade: Médio. Excelente para o primeiro hands-on.

"""