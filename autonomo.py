


"""
Olá! Com certeza. Que iniciativa excelente. Dado o seu background e o público-alvo (uma consultoria de tecnologia B2B como a Meta), podemos criar sugestões de software que sejam não apenas academicamente interessantes, mas que resolvam problemas de negócio reais que a equipe deles enfrenta no dia a dia.

A chave é conectar cada projeto a um pilar da atuação deles: otimizar operações internas, melhorar a entrega para clientes (SAP, Microsoft, etc.) ou criar novas ofertas de serviço.

Aqui estão 3 sugestões de softwares para desenvolver no workshop, com complexidade crescente, que cobrem todos os seus tópicos de maneira prática e coesa. Todos são baseados em Python, como você prefere.

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

Projeto 2: Analisador Inteligente de Requisições de Cliente e Gerador de Testes
Este projeto foca na eficiência operacional e na qualidade, algo crucial para uma consultoria.

O Problema de Negócio: Um novo projeto na Meta começa com uma requisição do cliente, muitas vezes escrita em linguagem natural e ambígua. A partir dela, analistas precisam criar especificações, e desenvolvedores precisam criar código e testes.

A Solução de IA: Uma ferramenta que recebe um texto de requisição do cliente e:

Analisa e Estrutura: Usa um LLM para extrair os requisitos funcionais, atores envolvidos e dados necessários, retornando uma saída estruturada (ex: JSON).
Gera Código (com Copilot): Usa a saída estruturada como um super-comentário no VS Code para que o GitHub Copilot gere o boilerplate do código (ex: classes Python, assinaturas de função).
Gera Testes Unitários: Usa um segundo LLM (ou uma ferramenta como CodiumAI) para ler o código gerado e criar um conjunto de testes unitários (pytest) que validam os requisitos.
Como se Conecta aos Tópicos do Workshop:

Eficiência Operacional: É o caso de uso perfeito para o GitHub Copilot, mostrando o ganho de produtividade.
Otimização de Testes e QA: Demonstra como a IA pode não só acelerar, mas também padronizar a criação de testes, cobrindo casos que um humano poderia esquecer.
Desenvolvimento com apoio de IAs Generativas: Atividade central do projeto.
Stack de Tecnologia Sugerido (Python):

Análise de Texto: Um script Python simples que usa a biblioteca openai ou anthropic para fazer a chamada à API do LLM com o prompt de análise.
Geração de Código: GitHub Copilot integrado diretamente no VS Code.
Geração de Testes: Outro script Python que faz uma chamada de API, enviando o código e pedindo por testes no formato pytest.
Framework de Teste: Pytest para executar os testes gerados.
Nível de Complexidade: Médio. Focado no fluxo de trabalho do desenvolvedor.

Projeto 3: Agente de IA para Automação de Processos de Negócio
Este é o projeto mais avançado, que introduz o conceito de agentes autônomos que podem tomar decisões e usar ferramentas.

O Problema de Negócio: Um cliente da Meta precisa automatizar um processo, como a triagem de pedidos de compra que chegam por e-mail. Hoje, isso é feito manualmente: alguém lê o e-mail, consulta o valor no SAP, verifica o estoque e aprova ou encaminha para um gerente.

A Solução de IA: Um Agente de IA que orquestra várias ferramentas para executar o processo:

O agente recebe o texto do e-mail.
Ele decide que precisa extrair o "produto" e a "quantidade".
Ele usa uma ferramenta (uma função Python simulada) para "consultar o ERP" sobre o preço daquele produto.
Com base no valor total, ele decide se pode aprovar automaticamente (ex: < R$ 1.000) ou se precisa usar outra ferramenta para "enviar e-mail para o gerente".
Como se Conecta aos Tópicos do Workshop:

Definição de Agentes de IA: É a materialização de um agente. Você explicará o que são reasoning, planning e tool use.
AIOps: Este é o gancho perfeito. Você pode discutir: "Ok, construímos este agente. Como o colocamos em produção de forma confiável?". Isso leva à conversa sobre MLOps/AIOps: versionamento do agente (código e prompts), esteiras de CI/CD (GitHub Actions) para testar os tools e o reasoning, e deployment em uma plataforma serverless (AWS Lambda, Azure Functions) que pode ser acionada por um novo e-mail.
Stack de Tecnologia Sugerido (Python):

Framework de Agentes: LangChain Agents ou Microsoft Semantic Kernel são os padrões para isso. Eles fornecem a lógica para o agente decidir qual ferramenta usar.
Ferramentas (Tools): Funções Python simples que simulam as ações (consultar_erp, enviar_email). No mundo real, elas fariam chamadas de API.
Modelo: Requer um LLM com boa capacidade de raciocínio, como GPT-4 ou Claude 3 Opus.
Demonstração de AIOps: Mostrar um arquivo workflow simples do GitHub Actions que executa testes no agente a cada commit.
Nível de Complexidade: Alto. Ideal para o final do workshop, unindo todos os conceitos.
"""