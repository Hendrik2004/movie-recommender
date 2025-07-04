import pandas as pd
import ast

def load_data(data_path="data/raw/"):
    """Se cargan los archivos necesarios desde la carpeta de datos."""
    print("Cargando datasets...")
    ratings = pd.read_csv(f"{data_path}ratings_small.csv")
    links = pd.read_csv(f"{data_path}links_small.csv")
    metadata = pd.read_csv(f"{data_path}movies_metadata.csv", low_memory=False)
    credits = pd.read_csv(f"{data_path}credits.csv")
    keywords = pd.read_csv(f"{data_path}keywords.csv")
    return ratings, links, metadata, credits, keywords

def clean_metadata(metadata):
    """Limpiar y filtrar el metadata de las películas (géneros, fechas, errores de tipo)."""
    print("Limpiando metadata...")
    metadata = metadata.copy()
    metadata = metadata.dropna(subset=["id", "title", "release_date", "genres"])
    metadata["id"] = pd.to_numeric(metadata["id"], errors="coerce")
    metadata = metadata.dropna(subset=["id"])
    metadata["release_year"] = pd.to_datetime(metadata["release_date"], errors="coerce").dt.year
    metadata["genres"] = metadata["genres"].apply(lambda x: [d['name'] for d in ast.literal_eval(x)] if pd.notna(x) else [])
    metadata["overview"] = metadata["overview"].fillna("")
    return metadata

def merge_datasets(links, metadata, credits, keywords):
    """Une los datasets usando el id de TMDB (de links) para construir un dataset enriquecido."""
    print("Unificando datasets...")
    links = links[["movieId", "tmdbId"]].dropna()
    links["tmdbId"] = pd.to_numeric(links["tmdbId"], errors="coerce")

    metadata = clean_metadata(metadata)
    credits["id"] = pd.to_numeric(credits["id"], errors="coerce")
    keywords["id"] = pd.to_numeric(keywords["id"], errors="coerce")

    # Unir metadata + créditos + keywords
    df = pd.merge(metadata, credits, left_on="id", right_on="id", how="left")
    df = pd.merge(df, keywords, on="id", how="left")

    # Unir con los IDs de MovieLens (movieId)
    df = pd.merge(links, df, left_on="tmdbId", right_on="id", how="left")

    print(f"Dataset enriquecido: {df.shape[0]} películas")
    return df

def extract_cast(df, top_n=3):
    """Extraer los primeros N actores del campo cast."""
    print("Extrayendo actores principales...")
    def get_top_cast(cast_json):
        try:
            cast = ast.literal_eval(cast_json)
            return [member['name'] for member in cast[:top_n]]
        except:
            return []
    df["top_cast"] = df["cast"].apply(get_top_cast)
    return df

def extract_keywords(df):
    """Extraer palabras clave del campo keywords."""
    print("Extrayendo palabras clave...")
    def get_keywords(keyword_json):
        try:
            kw = ast.literal_eval(keyword_json)
            return [k['name'] for k in kw]
        except:
            return []
    df["keywords_list"] = df["keywords"].apply(get_keywords)
    return df

def build_combined_text(df):
    """Crear un campo de texto combinado para modelos basados en contenido."""
    print("Combinando texto...")
    df["combined_text"] = (
        df["overview"].fillna('') + ' ' +
        df["genres"].apply(lambda x: ' '.join(x)).fillna('') + ' ' +
        df["top_cast"].apply(lambda x: ' '.join(x)).fillna('') + ' ' +
        df["keywords_list"].apply(lambda x: ' '.join(x)).fillna('')
    )
    return df

# Ejecución principal para prueba
if __name__ == "__main__":
    ratings, links, metadata, credits, keywords = load_data()
    enriched = merge_datasets(links, metadata, credits, keywords)
    enriched = extract_cast(enriched)
    enriched = extract_keywords(enriched)
    enriched = build_combined_text(enriched)

    print("\nEjemplo de película enriquecida:")
    print(enriched[["title", "genres", "top_cast", "keywords_list", "combined_text"]].head(1).to_string(index=False))
