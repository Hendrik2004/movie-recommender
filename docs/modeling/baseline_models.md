# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline, el cual corresponde a un modelo de clasificación supervisado usando regresión logística para predecir si a un usuario le gustará una película determinada.

## Descripción del modelo

El modelo baseline es un clasificador supervisado que utiliza **Regresión Logística**. Su objetivo es predecir si un usuario le dará una calificación positiva a una película.

## Variables de entrada

El modelo fue entrenado con dos tipos de características extraídas de las películas:

- **Sinopsis (`overview`)**:
  - Se aplicó vectorización TF-IDF para convertir la sinopsis en una representación numérica.
  - Se limitaron los vectores a un máximo de **500 términos representativos** (500 dimensiones).
  - Estas características capturan la relevancia de las palabras en el contexto del conjunto de datos.

- **Géneros (`genres`)**:
  - Se utilizó One-Hot Encoding para representar los géneros como variables binarias.
  - Cada género se codifica como una columna con valor `1` (presente) o `0` (ausente).
  - Géneros incluidos: `Action`, `Adventure`, `Animation`, `Comedy`, `Crime`, `Drama`, `Fantasy`, `Horror`, `Romance`, `Science Fiction`, `Thriller`, `War`, entre otros.


## Variable objetivo

- La variable objetivo (`target`) fue generada a partir de la columna `rating`:
  - `1` si la calificación del usuario es **mayor o igual a 4**.
  - `0` si la calificación es **menor a 4**.
  
  Esto convierte el problema en una clasificación binaria.

## Evaluación del modelo

### Métricas de evaluación

Para evaluar el desempeño del modelo, se utilizan las siguientes métricas:

- **Accuracy**: Proporción total de predicciones correctas.
- **Precision**: Proporción de positivos predichos que son realmente positivos.
- **Recall**: Proporción de positivos reales que fueron correctamente identificados.
- **F1-score**: Media armónica de precisión y recall.

### Resultados de evaluación

Resultados del modelo base: **Regresión Logística**.

| Clase        | Precision | Recall | F1-score | Support |
|--------------|-----------|--------|----------|---------|
| No le gustó  | 0.54      | 0.20   | 0.29     | 4,293   |
| Le gustó     | 0.54      | 0.84   | 0.66     | 4,700   |
|              |           |        |          |         |
| **Accuracy**                 |       |        | **0.54** | **8,993** |
| **Macro avg**               | 0.54  | 0.52   | 0.47     | 8,993   |
| **Weighted avg**            | 0.54  | 0.54   | 0.48     | 8,993   |


## Análisis de los resultados

Los resultados de este modelo muestran limitaciones claras:

- La **precisión general (accuracy)** del modelo es baja (54%), apenas por encima de un clasificador aleatorio.
- El modelo tiene un **fuerte sesgo hacia la clase "Le gustó"**, con un recall del 84% para esa clase, pero con una muy baja capacidad para identificar correctamente la clase "No le gustó" (recall del 20%).
- El **F1-score para la clase negativa** es particularmente bajo (0.29), lo que indica un mal desempeño al identificar correctamente las películas que no gustan.
- El desequilibrio en el desempeño sugiere que el modelo no está capturando bien las señales distintivas entre clases usando solo texto y géneros.


## Conclusiones

Este modelo baseline demuestra que una combinación de técnicas clásicas de PLN (TF-IDF) con codificación de categorías (géneros) puede generar un sistema de recomendación supervisado funcional. Aunque tiene limitaciones en términos de personalización, ofrece una base sólida sobre la cual comparar modelos más avanzados.
