# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** Recomendador de Películas (Clasificación Binaria)
- **Plataforma de despliegue:** Ejecución local con exposición vía Ngrok (prototipo). Opcionalmente desplegable en Railway o Render para entorno productivo.
- **Requisitos técnicos:** 
    - Python >= 3.10
    - FastAPI
    - Uvicorn
    - scikit-learn
    - joblib
    - pandas
    - pyngrok
    - Navegador web (para consumir la interfaz)
- **Requisitos de seguridad:** 
    - En entorno prototipo: ninguno (Ngrok genera una URL pública temporal).
    - En entorno productivo:
      - HTTPS obligatorio
      - Autenticación por token o cabeceras seguras
      - Registros de logs y auditoría
      
- **Diagrama de arquitectura:** (imagen que muestra la arquitectura del sistema que se utilizará para desplegar el modelo)

## Código de despliegue

- **Archivo principal:** scripts/deployment/main.py
- **Rutas de acceso a los archivos:** 
    - Modelos: models/*.joblib
    - Frontend: app.html
    - Script de exposición: scripts/deployment/ngrok_runner.py
- **Variables de entorno:** NGROK_AUTH_TOKEN (para usar una cuenta de Ngrok)

## Documentación del despliegue

- **Instrucciones de instalación:** 

1. Clonar el repositorio:
    git clone https://github.com/usuario/movie-recommender-clean.git
    cd movie-recommender-clean
2.Crear un entorno virtual 
    python -m venv venv
    venv\Scripts\activate
3. Instalar Dependencias
    pip install -r requirements.txt

- **Instrucciones de configuración:**

1. Asegurarse de tener entrenados los modelos en models/*.joblib
2. Definir la variable NGROK_AUTH_TOKEN para acceso prolongado:
    export NGROK_AUTH_TOKEN=INGRESAR_TOKEN
    
- **Instrucciones de uso:**   

1. Ejecutar el archivo ngrok_runner.py:
        python scripts/deployment/ngrok_runner.py
2. Esperar a que aparezca la URL pública de Ngrok en consola.
3. Abrir app.html en el navegador y usar el formulario para hacer predicciones.

- **Instrucciones de mantenimiento:**

1. Actualización del modelo: Reentrenar el modelo, sobrescribir el archivo .joblib y reiniciar el servidor.
2. Logs de errores: Ver en consola los errores lanzados por FastAPI o Uvicorn.
3. Despliegue en producción: Migrar main.py a un entorno con WSGI (Railway, Render, Heroku) y exponer app.html como recurso estático o desde un bucket (S3, Netlify, etc).
4. Revisión de seguridad: Asegurar HTTPS, control de cabeceras y validación estricta del input para ambientes reales.
