from pyngrok import ngrok
import uvicorn
import multiprocessing
import time
import os
import sys

# Asegurar que el path al proyecto raíz esté en sys.path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(project_root, "../..")))

# Importar la aplicación FastAPI
from scripts.deployment.main import app

# Establecer el token de autenticación de Ngrok si está definido
NGROK_AUTH_TOKEN = os.getenv("NGROK_AUTH_TOKEN")
if NGROK_AUTH_TOKEN:
    ngrok.set_auth_token(NGROK_AUTH_TOKEN)

# Iniciar el servidor Uvicorn en un proceso separado
def start_uvicorn():
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)

if __name__ == "__main__":
    p = multiprocessing.Process(target=start_uvicorn)
    p.start()
    time.sleep(3)  # Esperar a que el servidor se inicie

    # Crea túnel con Ngrok
    public_url = ngrok.connect(8000)
    print(f"\n La API está disponible en: {public_url} -> http://localhost:8000\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n Cerrando servidor...")
        p.terminate()
        ngrok.kill()
