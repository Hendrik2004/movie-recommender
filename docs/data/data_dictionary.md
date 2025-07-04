# Diccionario de datos

## Base de datos 1: ratings_small.csv

La siguiente tabla presenta las variables contenidas en el conjunto de datos ratings_small.csv. Este conjunto recopila calificaciones de 9000 películas realizadas por 700 usuarios. 

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| userId | Identificador único del usuario que hizo la calificación | Número entero (int64) | Números enteros positivos | MovieLens Dataset |
| movieId | Identificador único de la película calificada | Número entero (int64) | Números enteros positivos | MovieLens Dataset |
| rating | Calificación que el usuario da a la película | Número flotante (float64) | Flotantes desde 0.5 hasta 5.0 (pasos de 0.5) | MovieLens Dataset |
| timestamp | Fecha y hora que se hizo la calificación en formato UNIX | Número entero (int64) | Números enteros grandes | MovieLens Dataset |


- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Fuente de datos**: fuente de los datos de la variable.

## Base de datos 2: links.csv

La siguiente tabla presenta las variables incluidas en el archivo links.csv. Este archivo permite enlazar los identificadores de películas de MovieLens con sus correspondientes entradas en las bases de datos IMDb y TMDB.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| movieId | Identificador único de la película dentro del sistema MovieLens. | Número entero (int64) | Números enteros positivos | MovieLens Dataset |
| imdbId | Identificador único de la película en la base de datos IMDb. | Número entero (int64) | Números enteros positivos | MovieLens Dataset |
| tmdbId | Identificador único de la película en la base de datos TMDB | Número flotante (float64) | Números positivos | MovieLens Dataset |


- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Fuente de datos**: fuente de los datos de la variable.

