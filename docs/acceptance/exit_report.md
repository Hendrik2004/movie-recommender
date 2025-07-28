# Informe de salida

## Resumen Ejecutivo

Se construyó un sistema de recomendación de películas que predice si a un usuario le gustará una película basándose en su sinopsis y géneros. Para esto, se entrenaron y compararon cuatro modelos de clasificación: Logistic Regression, Random Forest, Gradient Boosting, SVM con kernel RBF.

## Resultados del proyecto

- Se exploraron y procesaron los datasets `ratings_small.csv` y `movies_metadata.csv` de MovieLens. Adicionalmente se graficarón diferentes distribuciones relacionadas a estos datos.
- Se entrenaron y compararon distintos modelos de aprendizaje automático, incluyendo:
  - Regresión logística
  - SVM con kernel RBF
  - Random Forest
  - Gradient Boosting
- Se desplegó una **API funcional usando FastAPI**, permitiendo realizar recomendaciones en tiempo real.
- La API fue expuesta mediante un túnel seguro utilizando **ngrok**, lo cual facilitó su prueba externa sin necesidad de infraestructura compleja.

## Lecciones aprendidas

- El preprocesamiento de datos fue crucial, especialmente al tratar con variables categóricas como los géneros de las películas.
- La integración de métodos colaborativos y basados en contenido mejora la cobertura y la precisión del sistema.
- Métricas como Precision@k y Recall@k ofrecen una evaluación más ajustada a los objetivos del sistema de recomendación que métricas genéricas como accuracy.
- El uso de FastAPI combinado con ngrok permite una demostración rápida y efectiva del modelo sin desplegar en la nube.


## Impacto del proyecto

- El sistema desarrollado replica la lógica de recomendación utilizada por plataformas de streaming como Netflix o Prime Video.
- Tiene potencial de ser aplicado en sectores como el entretenimiento, comercio electrónico, y plataformas de aprendizaje personalizado.
- Sienta las bases para escalar el sistema utilizando técnicas más avanzadas como embeddings, deep learning o datos enriquecidos desde APIs como TMDB o IMDb.

## Conclusiones

- Se logró implementar un sistema de recomendación funcional combinando modelos clásicos de machine learning con técnicas específicas del dominio.
- Incluso trabajando con un subconjunto reducido del dataset y recursos limitados, se logró una solución efectiva y escalable.
- El proyecto representa un ejemplo exitoso de aplicación de aprendizaje automático en un problema del mundo real, con potencial de mejora continua mediante nuevas fuentes de datos o metodologías más complejas.

## Agradecimientos

- Agradecimientos al equipo docente y a los compañeros del curso por su acompañamiento y retroalimentación durante las diferentes etapas del proyecto.

