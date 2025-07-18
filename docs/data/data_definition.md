# Definición de los Datos

##  Origen de los datos

Los datos utilizados en este proyecto provienen del conjunto **The Movies Dataset**, disponible en la plataforma de [Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset).

Se han utilizado dos conjuntos principales:

### 1. Calificaciones (versión reducida de MovieLens):
- `ratings_small.csv`: Calificaciones explícitas realizadas por usuarios a películas.
- `links_small.csv`: Relación entre los IDs de MovieLens, IMDb y TMDb.

### 2. Metadatos enriquecidos de TMDb:
- `movies_metadata.csv`: Información detallada de las películas como título, año, duración, idioma, géneros, presupuesto, etc.
- `credits.csv`: Información sobre el elenco y equipo de producción (actores, director).
- `keywords.csv`: Palabras clave asociadas a cada película.

Los archivos fueron descargados manualmente desde Kaggle y almacenados en la carpeta `data/raw/`.

---

##  Scripts para la carga de datos

- `scripts/data_acquisition/main.py`: Carga inicial de `ratings_small.csv` y `links_small.csv`.
- `scripts/enrichment/load_tmdb_metadata.py`: Carga y transformación de `movies_metadata.csv`, `credits.csv` y `keywords.csv`.

Estos scripts leen los archivos `.csv`, verifican su estructura y devuelven objetos `DataFrame` limpios para su posterior análisis.

---

##  Referencias a rutas y estructuras

### Rutas de origen de datos

- **Ubicación**:
  - `data/raw/ratings_small.csv`
  - `data/raw/links_small.csv`
  - `data/raw/movies_metadata.csv`
  - `data/raw/credits.csv`
  - `data/raw/keywords.csv`

- **Estructura de los archivos**:

| Archivo               | Descripción                                        |
|----------------------|----------------------------------------------------|
| `ratings_small.csv`  | `userId`, `movieId`, `rating`, `timestamp`         |
| `links_small.csv`    | `movieId`, `imdbId`, `tmdbId`                      |
| `movies_metadata.csv`| `id`, `title`, `genres`, `runtime`, `budget`, etc.|
| `credits.csv`        | `id`, `cast`, `crew` (en formato JSON)             |
| `keywords.csv`       | `id`, `keywords` (en formato JSON)                 |

- **Procesos de transformación aplicados**:
  - Conversión de campos `id` a enteros (cuando es posible).
  - Parseo de columnas JSON (`cast`, `crew`, `keywords`) a listas o estructuras planas.
  - Limpieza de valores nulos, duplicados o erróneos (`NaN`, presupuestos = 0).
  - Conversión de `timestamp` a formato de fecha legible.

---

### Base de datos de destino

- **Ubicación**: `data/processed/`
- **Archivos generados**:
  - `ratings_processed.csv`
  - `links_processed.csv`
  - `metadata_enriched.csv` (resultado de combinar los metadatos relevantes)
  - Otros archivos derivados para entrenamiento o visualización.

- **Estructura esperada**:
  - Variables limpias, con tipos de datos adecuados (`int`, `float`, `datetime`, `list`).
  - Campos semánticos para construir sistemas híbridos (colaborativo + contenido).

- **Procedimientos aplicados**:
  - Integración por `movieId` y `tmdbId`.
  - Normalización de información textual.
  - Enriquecimiento con características como géneros, actores principales, director, etc.

---

## ✅ Observaciones

Este proceso permite aumentar significativamente la capacidad del sistema de recomendación al incorporar información adicional sobre las películas, permitiendo enfoques híbridos y análisis exploratorios más completos.
