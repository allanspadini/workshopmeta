import pandas as pd
import matplotlib.pyplot as plt
from langgraph.graph import MessageGraph
from langchain_core.messages import HumanMessage, AIMessage

# === Configuração ===

# Parâmetros de degradação
ACCURACY_THRESHOLD = 0.85  # se accuracy < threshold → alerta

# === Funções do agente ===

# Node: ler os logs
def read_logs_node(messages):
    print("\n[ReadLogsNode] Lendo CSV de logs...")
    df = pd.read_csv("logs_inferencia.csv", parse_dates=["timestamp"])
    return {"messages": messages, "df_logs": df}

# Node: analisar performance
def analyze_performance_node(state):
    print("\n[AnalyzePerformanceNode] Analisando performance...")
    df_logs = state["df_logs"]
    
    # Simula "últimos N logs" → últimos 100
    df_recent = df_logs.tail(100)
    correct_preds = df_recent["predicted_label"] == df_recent["true_label"]
    accuracy = correct_preds.mean()
    
    print(f"Accuracy (últimos 100 logs): {accuracy:.2%}")
    
    # Grava no state
    state["accuracy"] = accuracy
    
    # (Opcional) salva gráfico para mostrar na aula
    df_logs["correct"] = df_logs["predicted_label"] == df_logs["true_label"]
    df_logs["rolling_accuracy"] = df_logs["correct"].rolling(window=100).mean()
    
    df_logs.plot(x="timestamp", y="rolling_accuracy", figsize=(12,6))
    plt.axhline(ACCURACY_THRESHOLD, color="red", linestyle="--", label="Threshold")
    plt.title("Rolling Accuracy (window=100)")
    plt.ylabel("Accuracy")
    plt.xlabel("Timestamp")
    plt.legend()
    plt.tight_layout()
    plt.savefig("accuracy_plot.png")
    print("Gráfico salvo como 'accuracy_plot.png'")
    
    return state

# Node: decisão (gera alerta ou não)
def decide_action_node(state):
    print("\n[DecideActionNode] Tomando decisão...")
    accuracy = state["accuracy"]
    messages = state["messages"]
    
    if accuracy < ACCURACY_THRESHOLD:
        msg = "⚠️ ALERTA: Performance degradada! Accuracy abaixo do threshold."
    else:
        msg = "✅ Performance OK."
    
    print(msg)
    
    # Adiciona mensagem para histórico
    messages.append(AIMessage(content=msg))
    
    return {"messages": messages}

# === Construção do LangGraph ===

graph = MessageGraph()

graph.add_node("read_logs", read_logs_node)
graph.add_node("analyze_performance", analyze_performance_node)
graph.add_node("decide_action", decide_action_node)

graph.set_entry_point("read_logs")
graph.add_edge("read_logs", "analyze_performance")
graph.add_edge("analyze_performance", "decide_action")
graph.set_finish_point("decide_action")

# === Compila o graph ===

app = graph.compile()

# === Executa ===

# Mensagem inicial (poderia vir de um trigger ou cronjob)
initial_messages = [HumanMessage(content="Executar monitoramento de performance")]

# Invoca o graph
response = app.invoke({"messages": initial_messages})

# Imprime histórico de mensagens
print("\n=== Histórico de mensagens do agente ===")
for msg in response["messages"]:
    tipo = msg.__class__.__name__
    conteudo = msg.content
    print(f"[{tipo}] {conteudo}\n")



