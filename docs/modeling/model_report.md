# Reporte del Modelo Final

## Resumen Ejecutivo

Se evaluaron tres modelos supervisados para predecir si a un usuario le gustará una película, usando información textual (sinopsis) y categórica (géneros). Las métricas de evaluación (precisión, recall, f1-score y accuracy) se compararon entre modelos para identificar el de mejor rendimiento. Los resultados fueron:

- **Logistic Regression**: accuracy de 0.54, con fuerte sesgo hacia la clase "Le gustó".
- **Random Forest**: accuracy de 0.57, mejorando el balance entre clases.
- **Gradient Boosting**: accuracy de 0.55, con recall alto pero baja precisión en la clase negativa.
- **SVM con kernel RBF**: accuracy de 0.57, balance similar al de Random Forest.

En términos generales, el modelo **Random Forest** fue el que presentó mejor equilibrio entre precisión y recall para ambas clases, siendo considerado como el modelo final recomendado para este problema, sin embargo, **SVM con kernel RBF** también muestra resultados muy cercanos.

## Descripción del Problema

El objetivo del proyecto es construir un sistema de recomendación supervisado que prediga si un usuario evaluará positivamente una película, basándose únicamente en sus características (sinopsis y géneros). 

Este enfoque es útil en situaciones donde no se dispone de información histórica detallada del usuario o cuando se desea predecir la aceptación de nuevos lanzamientos. El contexto del proyecto es un sistema de recomendación de películas en plataformas de streaming o sitios de crítica, donde es clave anticipar la satisfacción del usuario frente a nuevos contenidos.

## Descripción del Modelo

Se probaron cuatro algoritmos de clasificación:

1. **Regresión Logística** (baseline): modelo lineal simple, interpretativo y eficiente.
2. **Random Forest**: modelo basado en ensamblado de árboles, robusto a sobreajuste y capaz de manejar relaciones no lineales.
3. **Gradient Boosting**: técnica avanzada de boosting que construye árboles secuenciales minimizando el error.
4. **SVM con kernel RBF**: La idea principal del SVM es encontrar el hiperplano óptimo que mejor separa las clases en el espacio de características.


Todos los modelos utilizaron como entradas:

- **TF-IDF sobre la sinopsis** (`overview`) con 500 tokens más frecuentes.
- **Codificación binaria de géneros** (`genres`) mediante `MultiLabelBinarizer`.

La variable objetivo fue construida a partir del campo `rating`, donde:
- `le gustó` representa calificaciones **positivas** (rating ≥ 4).
- `no le gustó` representa calificaciones **negativas** (rating < 4).

## Evaluación del Modelo

A continuación se resumen los resultados de los tres modelos evaluados:

### Logistic Regression

| Clase        | Precisión | Recall | F1-score | Soporte |
|--------------|-----------|--------|----------|---------|
| No le gustó  | 0.54      | 0.20   | 0.29     | 4,293   |
| Le gustó     | 0.54      | 0.84   | 0.66     | 4,700   |
| **Accuracy**                 |       |        | **0.54** | **8,993** |
| **Macro avg**               | 0.54  | 0.52   | 0.47     | 8,993   |
| **Weighted avg**            | 0.54  | 0.54   | 0.48     | 8,993   |

### Random Forest

| Clase        | Precisión | Recall | F1-score | Soporte |
|--------------|-----------|--------|----------|---------|
| No le gustó  | 0.58      | 0.35   | 0.44     | 4,293   |
| Le gustó     | 0.57      | 0.77   | 0.65     | 4,700   |
| **Accuracy**                 |       |        | **0.57** | **8,993** |
| **Macro avg**               | 0.57  | 0.56   | 0.55     | 8,993   |
| **Weighted avg**            | 0.57  | 0.57   | 0.55     | 8,993   |

### Gradient Boosting

| Clase        | Precisión | Recall | F1-score | Soporte |
|--------------|-----------|--------|----------|---------|
| No le gustó  | 0.55      | 0.27   | 0.36     | 4,293   |
| Le gustó     | 0.55      | 0.80   | 0.65     | 4,700   |
| **Accuracy**                 |       |        | **0.55** | **8,993** |
| **Macro avg**               | 0.55  | 0.54   | 0.51     | 8,993   |
| **Weighted avg**            | 0.55  | 0.55   | 0.51     | 8,993   |

### SVM con kernel RBF

| Clase        | Precisión | Recall | F1-score | Soporte |
|--------------|-----------|--------|----------|---------|
| No le gustó  | 0.58      | 0.37   | 0.45     | 4,293   |
| Le gustó     | 0.57      | 0.76   | 0.65     | 4,700   |
| **Accuracy**                 |       |        | **0.57** | **8,993** |
| **Macro avg**               | 0.57  | 0.56   | 0.55     | 8,993   |
| **Weighted avg**            | 0.57  | 0.57   | 0.55     | 8,993   |

### Análisis

- **Random Forest** presentó el mejor equilibrio entre precisión y recall para ambas clases, especialmente en la clase "No le gustó".
- **Gradient Boosting** logró un recall alto en "Le gustó", pero a costa de una baja capacidad para detectar películas mal evaluadas.
- **Regresión Logística** mostró un fuerte sesgo hacia la clase positiva, con muy bajo recall para "No le gustó".
- **SVM con kernel RBF** logró una precisión general del 57%, mostrando un mejor equilibrio entre precisión y recall que modelos como la regresión logística o el gradient boosting.

## Conclusiones y Recomendaciones

- **Random Forest** se considera el mejor modelo baseline entre los evaluados por su equilibrio y mayor capacidad de generalización.
- Todos los modelos muestran un desempeño limitado en la clase "No le gustó", lo cual podría deberse a:
  - Desbalance de clases en los datos.
  - Baja capacidad discriminativa de las features utilizadas.

