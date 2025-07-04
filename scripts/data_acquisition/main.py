import pandas as pd

def load_movielens_data(path="data/raw/"):
    """Cargar los datos de MovieLens desde la carpeta 'data/raw/'."""
    try:
        ratings = pd.read_csv(f"{path}ratings_small.csv")
        links = pd.read_csv(f"{path}links_small.csv")
    except FileNotFoundError as e:
        print(f" Archivo no encontrado: {e.filename}")
        return None, None

    return ratings, links

if __name__ == "__main__":
    ratings, links = load_movielens_data()
    if ratings is not None and links is not None:
        print(" Muestras de ratings:")
        print(ratings.head())
        print("\n Muestras de links:")
        print(links.head())
    else:
        print("No se logró cargar los archivos.")
