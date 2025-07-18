import os
import pandas as pd
from scripts.data_acquisition.main import load_movielens_data

# Cargar los datos
ratings, links, metadata, credits, keywords = load_movielens_data()

# Validación
if any(x is None for x in [ratings, links, metadata, credits, keywords]):
    print("Error: Uno o más archivos no fueron cargados correctamente.")
    exit()

# === Preprocesar ratings ===
ratings.drop_duplicates(inplace=True)
ratings.dropna(inplace=True)
ratings["timestamp"] = pd.to_datetime(ratings["timestamp"], unit='s')

# === Preprocesar links ===
links.drop_duplicates(inplace=True)
links.dropna(inplace=True)
links["tmdbId"] = pd.to_numeric(links["tmdbId"], errors='coerce')

# === Preprocesar metadata ===
metadata = metadata.copy()
metadata = metadata[metadata["release_date"].notna()]
metadata["release_date"] = pd.to_datetime(metadata["release_date"], errors="coerce")
metadata["release_year"] = metadata["release_date"].dt.year
metadata["id"] = pd.to_numeric(metadata["id"], errors="coerce")
metadata = metadata.dropna(subset=["id"])
metadata["id"] = metadata["id"].astype(int)

# Guardar archivos preprocesados
ratings.to_csv("data/processed/ratings_processed.csv", index=False)
links.to_csv("data/processed/links_processed.csv", index=False)
metadata.to_csv("data/processed/movies_metadata_enriched.csv", index=False)

print("Todos los archivos preprocesados han sido guardados.")
