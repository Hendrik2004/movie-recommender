import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from scipy.sparse import hstack
import joblib
import ast
import os

# --- Leer datos procesados ---
metadata = pd.read_csv("data/processed/movies_metadata_enriched.csv")
ratings = pd.read_csv("data/processed/ratings_processed.csv")

# --- Parsear géneros ---
def parse_genres(genres_str):
    try:
        genres_list = ast.literal_eval(genres_str)
        return [genre['name'] for genre in genres_list if 'name' in genre]
    except:
        return []

metadata['parsed_genres'] = metadata['genres'].fillna('[]').apply(parse_genres)

# --- TF-IDF sobre overview ---
metadata['overview'] = metadata['overview'].fillna('')
tfidf = TfidfVectorizer(stop_words='english', max_features=500)
overview_tfidf = tfidf.fit_transform(metadata['overview'])

# --- One-hot de géneros ---
mlb = MultiLabelBinarizer()
genres_encoded = mlb.fit_transform(metadata['parsed_genres'])

# --- Fusionar metadata con ratings ---
df = pd.merge(ratings, metadata[['id', 'overview', 'parsed_genres']], how='inner', left_on='movieId', right_on='id')

# Aseguramos que el número de filas coincida para fusionar features
overview_final = tfidf.transform(df['overview'].fillna(''))
genres_final = mlb.transform(df['parsed_genres'])

# --- Combinar features en una matriz final ---
X = hstack([overview_final, genres_final])

# --- Guardar datos ---
os.makedirs("data/processed", exist_ok=True)

# Dataset completo para modelamiento supervisado
df_final = df[['userId', 'movieId', 'rating']]
df_final.loc[:, "genres"] = df['parsed_genres']
df_final.to_csv("data/processed/features_dataset.csv", index=False)

# Guardar features por separado (sparse)
joblib.dump(X, "data/processed/feature_matrix_sparse.joblib")
joblib.dump(tfidf, "data/processed/tfidf_vectorizer.joblib")
joblib.dump(mlb, "data/processed/mlb_genres.joblib")
