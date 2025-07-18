import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import ast

# Rutas
DATA_PATH = "data/processed/"
OUTPUT_PATH = "docs/data/"
os.makedirs(OUTPUT_PATH, exist_ok=True)

# === Carga de archivos ===
ratings = pd.read_csv(os.path.join(DATA_PATH, "ratings_processed.csv"))
links = pd.read_csv(os.path.join(DATA_PATH, "links_processed.csv"))
metadata = pd.read_csv(os.path.join(DATA_PATH, "movies_metadata_enriched.csv"))

# === Información general ===
print("=== Ratings ===")
print(ratings.info(), "\n", ratings.describe())

# === Limpieza de la columna 'genres' ===
metadata['genres_list'] = metadata['genres'].apply(
    lambda x: [d['name'] for d in ast.literal_eval(x)] if pd.notnull(x) and x != '[]' else []
)


metadata['main_genre'] = metadata['genres_list'].apply(lambda x: x[0] if len(x) > 0 else 'Unknown')

# === Información general ===
print("\n=== Metadata ===")
print(metadata.info())
print("\nResumen de 'main_genre' y 'release_year':")
print(metadata[['main_genre', 'release_year']].describe(include='all'))

# === Usuarios y películas ===
print(f"\nUsuarios únicos: {ratings['userId'].nunique()}")
print(f"Películas calificadas: {ratings['movieId'].nunique()}")

# === Distribución de ratings ===
plt.figure(figsize=(8, 4))
sns.countplot(x='rating', data=ratings)
plt.title('Distribución de Calificaciones')
plt.xlabel('Rating')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "rating_distribution.png"))
plt.close()

# === Promedio de ratings por usuario ===
avg_user = ratings.groupby('userId')['rating'].mean()
plt.figure(figsize=(8, 4))
sns.histplot(avg_user, bins=20, kde=True)
plt.title('Promedio de calificaciones por usuario')
plt.xlabel('Rating promedio')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "avg_rating_per_user.png"))
plt.close()

# === Número de calificaciones por película ===
ratings_per_movie = ratings['movieId'].value_counts()
plt.figure(figsize=(10, 5))
sns.histplot(ratings_per_movie, bins=50, log_scale=(True, False))  # x log, y normal
plt.title('Número de calificaciones por película')
plt.xlabel('Cantidad de calificaciones (escala log)')
plt.ylabel('Número de películas')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "ratings_per_movie_logscale.png"))
plt.close()

# Promedio de rating por género
ratings_genre = pd.merge(ratings, metadata[['id', 'genres_list']], left_on='movieId', right_on='id', how='left')
ratings_genre = ratings_genre.explode('genres_list')
avg_rating_per_genre = ratings_genre.groupby('genres_list')['rating'].mean().sort_values(ascending=False).head(15)

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_rating_per_genre.values, y=avg_rating_per_genre.index)
plt.title("Promedio de calificación por género (top 15)")
plt.xlabel("Calificación promedio")
plt.ylabel("Género")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "avg_rating_per_genre.png"))
plt.close()


# === Promedio de calificaciones por película ===
avg_movie = ratings.groupby("movieId")["rating"].mean()
plt.figure(figsize=(8, 4))
sns.histplot(avg_movie, bins=20, kde=True)
plt.title("Promedio de calificaciones por película")
plt.xlabel("Calificación promedio")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "avg_rating_per_movie.png"))
plt.close()

# === Distribución de géneros ===
genre_counts = metadata['genres_list'].explode().value_counts().head(15)
plt.figure(figsize=(10, 6))
sns.barplot(x=genre_counts.values, y=genre_counts.index)
plt.title("Películas por género (top 15)")
plt.xlabel("Cantidad de películas")
plt.ylabel("Género")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "genres_distribution.png"))
plt.close()

# === Distribución por año de lanzamiento ===
plt.figure(figsize=(10, 5))
sns.histplot(metadata['release_year'].dropna(), bins=40, kde=False)
plt.title("Distribución de películas por año de lanzamiento")
plt.xlabel("Año")
plt.ylabel("Cantidad de películas")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "release_year_distribution.png"))
plt.close()


# === Matriz de correlación ===

# Unir ratings con metadata
metadata['id'] = metadata['id'].astype(int)
ratings_merged = pd.merge(ratings, metadata, left_on='movieId', right_on='id', how='left')

# Crear variables transformadas
ratings_merged['budget_log'] = ratings_merged['budget'].apply(lambda x: np.log1p(x))
ratings_merged['revenue_log'] = ratings_merged['revenue'].apply(lambda x: np.log1p(x))

# Seleccionar columnas relevantes
enriched_vars = [
    'rating', 'release_year', 'runtime', 'popularity',
    'vote_average', 'vote_count', 'budget_log', 'revenue_log'
]

# Eliminar nulos
corr_data = ratings_merged[enriched_vars].dropna()

# Calcular y graficar matriz
plt.figure(figsize=(10, 8))
corr_matrix_enriched = corr_data.corr()
sns.heatmap(corr_matrix_enriched, annot=True, cmap="coolwarm", fmt=".2f", center=0)
plt.title("Matriz de correlación (variables enriquecidas)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_PATH, "correlation_matrix_enriched.png"))
plt.close()

print("Análisis exploratorio completado. Gráficas generadas en docs/data/")
