import pandas as pd
import joblib
import os
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

# === Cargar dataset de features procesadas ===
df = pd.read_csv("data/processed/features_dataset.csv")
df["genres"] = df["genres"].apply(eval)

# === Preparar X e y ===
X = df.drop(columns=["userId", "movieId", "rating"])
y = (df["rating"] >= 4).astype(int)  # Clasificación binaria

# One-hot de géneros
mlb = MultiLabelBinarizer()
genres_encoded = pd.DataFrame(mlb.fit_transform(X["genres"]), columns=mlb.classes_)
X = X.drop(columns=["genres"]).reset_index(drop=True)
X = pd.concat([X, genres_encoded], axis=1)

# División entrenamiento/prueba 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# === Cargar modelos entrenados ===
model_dir = "models"
model_files = [f for f in os.listdir(model_dir) if f.endswith(".joblib")]

# === Evaluación de cada modelo ===
results = []

for model_file in model_files:
    model_path = os.path.join(model_dir, model_file)
    model = joblib.load(model_path)

    y_pred = model.predict(X_test)

    results.append({
        "Modelo": model_file.replace(".joblib", ""),
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1-score": f1_score(y_test, y_pred),
    })

# === Mostrar resultados ===
results_df = pd.DataFrame(results).sort_values(by="F1-score", ascending=False)
print("=== Comparación de modelos ===\n")
print(results_df.to_string(index=False))

#  Guardar a CSV
results_df.to_csv("docs/data/model_evaluation_summary.csv", index=False)



# === Visualización de métricas ===
metricas = ["Accuracy", "Precision", "Recall", "F1-score"]

for metrica in metricas:
    plt.figure(figsize=(8, 5))
    sns.barplot(data=results_df, x=metrica, y="Modelo", palette="viridis")
    plt.title(f"Comparación de modelos según {metrica}")
    plt.xlabel(metrica)
    plt.ylabel("Modelo")
    plt.xlim(0, 1)  # Métricas entre 0 y 1
    plt.tight_layout()

    # Guardar gráfico
    plot_path = f"docs/data/metric_{metrica.lower()}.png"
    plt.savefig(plot_path)
    plt.close()

# === Ranking total de modelos  ===

# Calcular ranking por métrica
ranking_df = results_df.copy()
for metric in ["Accuracy", "Precision", "Recall", "F1-score"]:
    ranking_df[f"{metric}_rank"] = ranking_df[metric].rank(ascending=False)

# Promediar el ranking de cada modelo
ranking_df["Average_Rank"] = ranking_df[
    ["Accuracy_rank", "Precision_rank", "Recall_rank", "F1-score_rank"]
].mean(axis=1)

# Ordenar modelos por ranking
ranking_df = ranking_df.sort_values("Average_Rank")

# Visualización
plt.figure(figsize=(8, 5))
sns.barplot(data=ranking_df, x="Average_Rank", y="Modelo", palette="magma_r")
plt.title("Ranking Promedio de Modelos")
plt.xlabel("Ranking Promedio (↓ mejor)")
plt.ylabel("Modelo")
plt.tight_layout()
plt.savefig("docs/data/overall_model_ranking.png")
plt.close()


