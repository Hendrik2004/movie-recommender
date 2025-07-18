#  Sistema de Recomendación de Películas

Este proyecto implementa un sistema de recomendación de películas basado en el dataset MovieLens enriquecido con metadatos de TMDB. Se desarrolló como parte del curso de **Metodologías Ágiles** (Módulo 6) de la Maestría en Ingeniería de Sistemas de la Universidad Nacional de Colombia.

---

##  Objetivo

Recomendar películas personalizadas a los usuarios en función de sus calificaciones previas, utilizando enfoques colaborativos y de contenido.  
La incorporación de metadatos busca mejorar la calidad y diversidad de las recomendaciones.

---

##  Estructura del proyecto (TDSP)

- `src/`: Código fuente del sistema.
- `scripts/`: Notebooks y scripts de ejecución.
- `docs/`: Documentación estructurada (CRISP-DM).
- `data/raw/`: Datos originales descargados (MovieLens + TMDB).
- `data/processed/`: Datos preprocesados para entrenamiento y análisis.

---

##  Tecnologías

- Python (pandas, scikit-learn, matplotlib, seaborn)
- Jupyter Notebooks
- Git & GitHub
- MLflow (fases posteriores)

---

##  Dataset

El proyecto utiliza los siguientes archivos del [The Movies Dataset - Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset):

### Datos utilizados inicialmente
- `ratings_small.csv`: Calificaciones explícitas por parte de usuarios.
- `links_small.csv`: Relación entre IDs de MovieLens, IMDb y TMDb.

### Nuevos archivos integrados
- `movies_metadata.csv`: Título, año, duración, idioma, géneros, sinopsis, presupuesto, etc.
- `credits.csv`: Elenco principal y director de cada película.
- `keywords.csv`: Palabras clave asociadas a cada película.

La fusión de estos datos permite construir modelos más complejos y generar visualizaciones más informativas.

---

## 👥 Autores

- **Hendrik Olaya Castro** — heolayac@unal.edu.co  
- **Alejandro Martín Salcedo** — almartins@unal.edu.co



