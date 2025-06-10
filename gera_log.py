import pandas as pd
import random
from datetime import datetime, timedelta

# Parâmetros
n_logs = 500
start_date = datetime(2025, 6, 1, 8, 0, 0)

# Possíveis textos
positive_texts = [
    "Produto muito bom, gostei",
    "Excelente atendimento",
    "Super recomendo",
    "Muito satisfeito com a compra",
    "Entrega rápida e produto perfeito"
]

negative_texts = [
    "Não funcionou direito",
    "Péssima qualidade",
    "Muito ruim, não recomendo",
    "Produto chegou quebrado",
    "Experiência horrível"
]

# Simula degradação de performance ao longo do tempo
degradation_start = int(n_logs * 0.6)  # a partir de 60% dos logs
flip_probability = 0.1  # chance de erro no começo
flip_probability_end = 0.4  # chance de erro no fim (simula degradação)

# Gera logs
logs = []
for i in range(n_logs):
    timestamp = start_date + timedelta(minutes=i * 5)
    
    if random.random() < 0.5:
        input_text = random.choice(positive_texts)
        true_label = "positive"
    else:
        input_text = random.choice(negative_texts)
        true_label = "negative"
    
    # Simula degradação progressiva
    if i < degradation_start:
        prob_flip = flip_probability
    else:
        # aumenta progressivamente até flip_probability_end
        progress = (i - degradation_start) / (n_logs - degradation_start)
        prob_flip = flip_probability + progress * (flip_probability_end - flip_probability)
    
    # Decide se vai flipar a predição
    if random.random() < prob_flip:
        predicted_label = "negative" if true_label == "positive" else "positive"
    else:
        predicted_label = true_label
    
    latency_ms = random.randint(100, 200)
    confidence = round(random.uniform(0.7, 1.0), 2)
    
    logs.append([timestamp, input_text, predicted_label, true_label, latency_ms, confidence])

# Cria DataFrame
df_logs = pd.DataFrame(logs, columns=["timestamp", "input_text", "predicted_label", "true_label", "latency_ms", "confidence"])

# Salva em CSV
df_logs.to_csv("logs_inferencia.csv", index=False)

print("Logs gerados e salvos como 'logs_inferencia.csv'")
