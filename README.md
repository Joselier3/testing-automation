# Guía de Instalación

Esta guía te ayudará a configurar el entorno necesario para ejecutar el programa de automatización de formularios.

## Instalación del Gestor de Paquetes (uv)

1. **Windows**:
   - Abre el Símbolo del sistema (cmd)
   - Copia y pega el siguiente comando:
     ```
     powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
     ```

2. **Linux**:
   - Abre una terminal
   - Copia y pega el siguiente comando:
     ```
     curl -LsSf https://astral.sh/uv/install.sh | sh
     ```

3. Verifica la instalación escribiendo:
   ```
   uv --version
   ```
   Deberías ver un número de versión

## Configuración del Entorno Virtual

1. Crea un directorio para el proyecto
2. Abre una terminal en ese directorio
3. Ejecuta los siguientes comandos en orden:

   ```
   # Crear el entorno virtual
   uv venv --python 3.11

   # Activar el entorno virtual
   source .venv/bin/activate  # Linux
   .venv\Scripts\activate     # Windows
   ```
   Verás que el prompt cambia para mostrar `(.venv)` al inicio

4. Para desactivar el entorno virtual cuando termines, escribe:
   ```
   deactivate
   ```

## Instalación de Dependencias

1. Asegúrate de que el entorno virtual está activado (deberías ver `(.venv)` al inicio del prompt)
2. Instala las dependencias del proyecto:
   ```
   uv pip install -r requirements.txt
   ```

## Instalación de Playwright

1. Con el entorno virtual activado, ejecuta:
   ```
   uvx playwright install
   ```
   - Este proceso descargará Chromium (aproximadamente 200MB)
   - Asegúrate de tener conexión a internet
   - El proceso puede tardar varios minutos

## Configuración de la API Key

1. En el directorio del proyecto, crea un nuevo archivo llamado `.env`
2. Abre el archivo con un editor de texto
3. Añade la siguiente línea:
   ```
   OPENAI_API_KEY=tu_clave_api_aquí
   ```
   Reemplaza `tu_clave_api_aquí` con tu clave de API de OpenAI

## Ejecución del Programa

1. Asegúrate de que el entorno virtual está activado
2. Ejecuta:
   ```
   uv run agent.py
   ```

## Solución de Problemas Comunes

- **Error al instalar uv**: 
  - Intenta ejecutar el comando de instalación nuevamente
  - Asegúrate de tener conexión a internet

- **Error al activar el entorno virtual**:
  - Asegúrate de estar en el directorio correcto
  - Verifica que el directorio `.venv` existe

- **Error al instalar dependencias**:
  - Verifica que el entorno virtual está activado
  - Asegúrate de tener conexión a internet

- **Error al ejecutar el programa**:
  - Verifica que el archivo `.env` existe y contiene la clave API correcta
  - Asegúrate de que todas las dependencias están instaladas

## Para Detener el Programa

Presiona `Ctrl + C` en la terminal donde se está ejecutando el programa.
