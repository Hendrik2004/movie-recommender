# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

**Sistema de Recomendación de Películas con MovieLens**

## Objetivo del Proyecto

El objetivo de este proyecto es desarrollar un sistema de recomendación de películas 
que sugiera títulos relevantes a los usuarios en función de sus calificaciones previas,
utilizando el conjunto de datos público MovieLens.

Este sistema busca replicar la lógica de las plataformas de streaming modernas,
mejorando la experiencia del usuario mediante la aplicación de modelos de recomendación colaborativos
y basados en contenido utilizando  la información disponible en MovieLens.


## Alcance del Proyecto

### Incluye:

- Uso del dataset **MovieLens (ratings_small.csv y movies.csv)** con calificaciones explícitas de usuarios y metadatos básicos como títulos y géneros.
- Exploración y análisis de los datos de usuarios y películas.
- Construcción de modelos de recomendación:
  - Colaborativo (basado en similitud entre usuarios o ítems)
  - Basado en contenido (utilizando géneros como atributos)
- Evaluación del sistema mediante métricas como precision@k y recall@k

### Excluye:

- Enriquecimiento con fuentes externas (como TMDB o IMDb).
- Despliegue en producción o integración con sistemas externos.
- Recolección de datos en tiempo real.

## Metodología

Se empleará la metodología **CRISP-DM**, adaptada al desarrollo de proyectos de ciencia de datos:

1. Comprensión del negocio
2. Comprensión de los datos
3. Preparación de los datos
4. Modelado (colaborativo y basado en contenido)
5. Evaluación (métricas de precisión y cobertura)
6. Despliegue (fase opcional)

## Cronograma

| Etapa                                      | Duración Estimada  | Fechas estimadas             |
|--------------------------------------------|--------------------|------------------------------|
| Entendimiento del negocio y carga de datos | 1 semana           | 25 - 03 de julio             |
| Preprocesamiento, análisis exploratorio    | 1 semana           | 02 - 10 de julio             |
| Modelamiento y recomendaciones             | 1 semana           | 09 - 17 de julio             |
| Evaluación de resultados                   | 1 semana           | 16 - 24 de julio             |
| Entrega final del proyecto                 | 1 semana           | 23 - 31 de julio             |

## Equipo del Proyecto

- **Alejandro Martin Salcedo - Email: almartins@unal.edu.co**
- **Hendrik Olaya Castro - Email: heolayac@unal.edu.co**

## Presupuesto

Proyecto académico – sin presupuesto asignado.  
Uso exclusivo de herramientas y bibliotecas de código abierto (Python, pandas, scikit-learn, Jupyter, GitHub).

## Stakeholders

- **Docentes del curso** – Revisores y evaluadores del proceso.
- **Compañeros del curso** – Posibles usuarios del sistema.
- **Entorno simulado de plataformas de recomendación** – Contexto de aplicación del modelo.

## Aprobaciones

- **Juan Sebastián Malagón Torres (Evaluador)**
- **Firma:** ______________________  
- **Fecha de aprobación:** ______________________

