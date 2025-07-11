import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ruta a los datos procesados
DATA_PATH = "data/processed/"
OUTPUT_PATH = "docs/data/"

# Crear la carpeta de salida si no existe
os.makedirs(OUTPUT_PATH, exist_ok=True)

# Carga de  datos
ratings = pd.read_csv(os.path.join(DATA_PATH, "ratings_processed.csv"))
links = pd.read_csv(os.path.join(DATA_PATH, "links_processed.csv"))

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

# Promedio de calificaciones por película
avg_rating_per_movie = ratings.groupby("movieId")["rating"].mean()
plt.figure(figsize=(8, 4))
sns.histplot(avg_rating_per_movie, bins=20, kde=True)
plt.title("Distribución de promedio de calificaciones por película")
plt.xlabel("Calificación promedio")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "avg_rating_per_movie.png"))
plt.close()

print("Análisis exploratorio completado. Gráficas guardadas en docs/data/")
