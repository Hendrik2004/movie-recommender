import pandas as pd

def load_movielens_data(path="data/raw/"):
    """
    Cargar los archivos de MovieLens y TMDB desde la carpeta 'data/raw/'.

    Archivos esperados:
        - ratings_small.csv
        - links_small.csv
        - movies_metadata.csv
        - credits.csv
        - keywords.csv
    """
    try:
        ratings = pd.read_csv(f"{path}ratings_small.csv")
        links = pd.read_csv(f"{path}links_small.csv")
        metadata = pd.read_csv(f"{path}movies_metadata.csv", low_memory=False)
        credits = pd.read_csv(f"{path}credits.csv")
        keywords = pd.read_csv(f"{path}keywords.csv")
    except FileNotFoundError as e:
        print(f"Archivo no encontrado: {e.filename}")
        return None, None, None, None, None

    return ratings, links, metadata, credits, keywords

if __name__ == "__main__":
    ratings, links, metadata, credits, keywords = load_movielens_data()

    if all(x is not None for x in (ratings, links, metadata, credits, keywords)):
        print("Muestras de ratings:")
        print(ratings.head())
        print("\nMuestras de links:")
        print(links.head())
        print("\nMuestras de metadata:")
        print(metadata[['id', 'title', 'genres', 'release_date']].head())
        print("\nMuestras de credits:")
        print(credits[['id', 'cast', 'crew']].head())
        print("\nMuestras de keywords:")
        print(keywords[['id', 'keywords']].head())
    else:
        print("No se logró cargar uno o más archivos.")
