import os
import pandas as pd
from scripts.data_acquisition.main import load_movielens_data


# Cargar datos
ratings, links = load_movielens_data()

if ratings is None or links is None:
    print("Error cargando los datos.")
    exit()

# Preprocesamiento de ratings
ratings.drop_duplicates(inplace=True)
ratings.dropna(inplace=True)
ratings["userId"] = ratings["userId"].astype(int)
ratings["movieId"] = ratings["movieId"].astype(int)
ratings["rating"] = ratings["rating"].astype(float)
ratings["timestamp"] = pd.to_datetime(ratings["timestamp"], unit='s')

# Preprocesamiento de links
links.drop_duplicates(inplace=True)
links.dropna(inplace=True)
links["movieId"] = links["movieId"].astype(int)
links["imdbId"] = links["imdbId"].astype(str)
links["tmdbId"] = pd.to_numeric(links["tmdbId"], errors='coerce')

# Guardar datos procesados
ratings.to_csv("data/processed/ratings_processed.csv", index=False)
links.to_csv("data/processed/links_processed.csv", index=False)

print("Datos preprocesados guardados.")
