import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Rutas
DATA_PATH = "data/processed/"
OUTPUT_PATH = "docs/data/"
os.makedirs(OUTPUT_PATH, exist_ok=True)

# Validar existencia de los archivos
ratings_file = os.path.join(DATA_PATH, "ratings_processed.csv")
links_file = os.path.join(DATA_PATH, "links_processed.csv")

if not os.path.exists(ratings_file):
    raise FileNotFoundError(f"{ratings_file} no encontrado.")
if not os.path.exists(links_file):
    raise FileNotFoundError(f"{links_file} no encontrado.")

# Carga de datos
ratings = pd.read_csv(ratings_file)
links = pd.read_csv(links_file)

# Información general
print("=== Información de ratings ===")
print(ratings.info())
print("\n=== Descripción de ratings ===")
print(ratings.describe())

print("\n=== Información de links ===")
print(links.info())

# Número de usuarios y películas
n_users = ratings['userId'].nunique()
n_movies = ratings['movieId'].nunique()
print(f"\nNúmero de usuarios únicos: {n_users}")
print(f"Número de películas únicas calificadas: {n_movies}")

# Distribución de ratings
plt.figure(figsize=(8, 4))
sns.countplot(x='rating', data=ratings)
plt.title('Distribución de calificaciones')
plt.xlabel('Rating')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "rating_distribution.png"))
plt.close()

# Promedio de ratings por usuario
avg_ratings_per_user = ratings.groupby('userId')['rating'].mean()
plt.figure(figsize=(8, 4))
sns.histplot(avg_ratings_per_user, bins=20, kde=True)
plt.title('Promedio de calificaciones por usuario')
plt.xlabel('Rating promedio')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "avg_rating_per_user.png"))
plt.close()

# Calificaciones por película (popularidad)
ratings_per_movie = ratings['movieId'].value_counts()
plt.figure(figsize=(8, 4))
sns.histplot(ratings_per_movie, bins=50, log_scale=True)
plt.title('Distribución de número de calificaciones por película')
plt.xlabel('Cantidad de calificaciones')
plt.ylabel('Número de películas')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "ratings_per_movie.png"))
plt.close()

# Heatmap de correlación (en este caso solo 'rating')
plt.figure(figsize=(6, 4))
sns.heatmap(ratings[['rating']].corr(), annot=True, cmap='coolwarm')
plt.title("Matriz de correlación (ratings)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "correlation_heatmap.png"))
plt.close()

# Películas más calificadas (Top 5)
top_movies = ratings['movieId'].value_counts().head(5)
print("\nPelículas con más calificaciones:")
print(top_movies)

print("\n Análisis exploratorio completado. Gráficas guardadas en 'docs/data/'")
