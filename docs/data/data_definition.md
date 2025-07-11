# Definición de los Datos

## Origen de los datos

- Los datos utilizados en este proyecto provienen del conjunto **The Movies Dataset**, disponible en la plataforma de [Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset). 
- Para este proyecto se utilizaron únicamente dos archivos en su versión reducida:
  - `ratings_small.csv`: contiene calificaciones explícitas realizadas por usuarios a películas.
  - `links_small.csv`: permite enlazar los IDs de MovieLens con los correspondientes en IMDb y TMDb.
- Los datos fueron descargados manualmente desde Kaggle y almacenados localmente en la carpeta `data/raw/`.

## Especificación de los scripts para la carga de datos

- El script responsable de la carga inicial de los datos es:
  - `scripts/data_acquisition/main.py`
- Este script se encarga de leer los archivos `.csv` desde la carpeta de datos crudos (`data/raw/`) y verificar su estructura básica antes de su procesamiento posterior.

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos

- **Ubicación**:
  - Los archivos de origen se encuentran en `data/raw/`.
  - Archivos específicos:
    - `data/raw/ratings_small.csv`
    - `data/raw/links_small.csv`

- **Estructura de los archivos**:
  - Archivos en formato `.csv` separados por comas, con encabezado en la primera fila.
  - `ratings_small.csv`: columnas `userId`, `movieId`, `rating`, `timestamp`.
  - `links_small.csv`: columnas `movieId`, `imdbId`, `tmdbId`.

- **Procedimientos de transformación y limpieza**:
  - Conversión de tipos de datos (por ejemplo, timestamps a fechas).
  - Eliminación de valores nulos o duplicados.
  - Estandarización de identificadores para enlazar datos entre archivos.

### Base de datos de destino

- **Ubicación**:
  - La base de datos de destino se simula mediante almacenamiento local en archivos `.csv` dentro de la carpeta `data/processed/`.

- **Estructura**:
  - Archivos preprocesados listos para análisis y modelado.
  - Se espera que los datos estén limpios, sin valores faltantes y con las variables necesarias transformadas.

- **Procedimientos aplicados**:
  - Filtrado de columnas no relevantes.
  - Enlace entre calificaciones y metadatos de películas usando `movieId`.
  - Creación de estructuras de datos listas para los modelos de recomendación.
