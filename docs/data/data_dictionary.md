# Diccionario de Datos

## Base de datos 1: `ratings_small.csv`

Este conjunto recopila calificaciones de aproximadamente 9.000 películas por parte de 700 usuarios.

| Variable   | Descripción                                                   | Tipo de dato     | Rango / Valores posibles               | Fuente de datos       |
|------------|---------------------------------------------------------------|------------------|----------------------------------------|------------------------|
| userId     | ID único del usuario que realiza la calificación              | int64            | Enteros positivos                      | MovieLens Dataset      |
| movieId    | ID único de la película                                       | int64            | Enteros positivos                      | MovieLens Dataset      |
| rating     | Calificación otorgada a la película                           | float64          | De 0.5 a 5.0 (pasos de 0.5)            | MovieLens Dataset      |
| timestamp  | Marca de tiempo UNIX de la calificación                       | int64 → datetime | Fechas entre 2000 y 2016 (aprox)       | MovieLens Dataset      |

---

## Base de datos 2: `links_small.csv`

Enlaza los identificadores internos de MovieLens con los de IMDb y TMDb.

| Variable   | Descripción                                                   | Tipo de dato     | Rango / Valores posibles               | Fuente de datos       |
|------------|---------------------------------------------------------------|------------------|----------------------------------------|------------------------|
| movieId    | ID interno de la película en MovieLens                        | int64            | Enteros positivos                      | MovieLens Dataset      |
| imdbId     | ID de la película en IMDb                                     | string            | Formato numérico (e.g., "0114709")     | MovieLens Dataset      |
| tmdbId     | ID de la película en TMDb                                     | float64 → int    | Enteros positivos o `NaN`              | MovieLens Dataset      |

---

## Base de datos 3: `movies_metadata.csv`

Contiene información detallada sobre las películas.

| Variable         | Descripción                                                 | Tipo de dato   | Ejemplos / Valores posibles                          | Fuente de datos |
|------------------|-------------------------------------------------------------|----------------|------------------------------------------------------|-----------------|
| id               | ID de la película en TMDb                                   | int64 (str)    | "862", "8844", etc.                                  | TMDb            |
| title            | Título original de la película                              | string         | "Toy Story", "Jumanji"                               | TMDb            |
| genres           | Lista de géneros (en formato JSON)                          | string/list    | `[{"id": 16, "name": "Animation"}, ...]`             | TMDb            |
| original_language| Idioma original de la película                              | string         | "en", "fr", "es"                                     | TMDb            |
| release_date     | Fecha de estreno                                            | string         | "1995-10-30"                                         | TMDb            |
| runtime          | Duración en minutos                                         | float64        | 90, 120, `NaN`                                       | TMDb            |
| vote_average     | Calificación promedio en TMDb                               | float64        | 0.0 - 10.0                                           | TMDb            |
| vote_count       | Número total de votos en TMDb                               | int64          | 0 - 50.000+                                          | TMDb            |
| budget           | Presupuesto estimado en USD                                 | int64          | 0 - 300.000.000                                      | TMDb            |
| revenue          | Ingresos estimados en USD                                   | int64          | 0 - 2.700.000.000                                    | TMDb            |
| status           | Estado de la película                                       | string         | "Released", "Post Production", etc.                  | TMDb            |

---

## Base de datos 4: `credits.csv`

Presenta información sobre el reparto y equipo técnico de cada película.

| Variable   | Descripción                                                   | Tipo de dato     | Ejemplos / Detalles                                  | Fuente de datos |
|------------|---------------------------------------------------------------|------------------|------------------------------------------------------|-----------------|
| id         | ID de la película (coincide con TMDb)                         | int64            | 862, 8844                                            | TMDb            |
| cast       | Lista de actores principales (formato JSON)                   | list[string]     | Nombres y roles: actor, personaje                    | TMDb            |
| crew       | Lista del equipo técnico (formato JSON)                       | list[string]     | Incluye director, productores, etc.                  | TMDb            |

> Para efectos del análisis, se extraen los **3 actores principales** y el **director**.

---

## Base de datos 5: `keywords.csv`

Contiene las palabras clave asociadas a cada película.

| Variable   | Descripción                                                   | Tipo de dato     | Ejemplos / Detalles                                  | Fuente de datos |
|------------|---------------------------------------------------------------|------------------|------------------------------------------------------|-----------------|
| id         | ID de la película en TMDb                                     | int64            | 862, 8844                                            | TMDb            |
| keywords   | Lista de palabras clave asociadas (formato JSON)              | list[string]     | "future", "space travel", "friendship", etc.         | TMDb            |

---

