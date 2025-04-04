# Guía de Instalación

Esta guía te ayudará a configurar el entorno necesario para ejecutar el programa de automatización de formularios.

## Obtención del Código del Proyecto

1. **Descarga el proyecto**:
   - Visita el repositorio del proyecto
   - Haz clic en el botón "Code" y selecciona "Download ZIP"
   - Extrae el archivo ZIP en una ubicación de tu preferencia (por ejemplo, en el Escritorio)
   - La carpeta extraída se llamará 'testing-automation'

## Requisitos Previos

1. **Python 3.11**
   - Si no tienes Python instalado:
     1. Visita [python.org/downloads](https://www.python.org/downloads/)
     2. Descarga la versión 3.11.x para Windows
     3. Durante la instalación, marca la casilla "Add Python to PATH"
     4. Verifica la instalación abriendo el Símbolo del sistema y escribiendo:
        ```
        python --version
        ```
        Deberías ver "Python 3.11.x"

## Instalación del Gestor de Paquetes (uv)

1. Abre el Símbolo del sistema (cmd)
2. Copia y pega el siguiente comando:
   ```
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
3. **Importante**: Cierra y vuelve a abrir el Símbolo del sistema para que los cambios en el PATH surtan efecto
4. Verifica la instalación escribiendo:
   ```
   uv --version
   ```
   Deberías ver un número de versión

## Configuración del Entorno Virtual

1. **Abre el Símbolo del sistema en el directorio del proyecto**:
   - Método 1 (Recomendado):
     1. Abre el Explorador de Windows
     2. Navega hasta la carpeta 'testing-automation'
     3. En la barra de direcciones, escribe 'cmd' y presiona Enter
   
   - Método 2 (Alternativo):
     1. Abre el Explorador de Windows
     2. Navega hasta la carpeta 'testing-automation'
     3. Haz clic derecho en un espacio vacío de la carpeta
     4. Selecciona "Abrir la ventana de comandos aquí"

2. Verifica que estás en el directorio correcto:
   ```
   cd
   ```
   Deberías ver la ruta que termina en 'testing-automation'

3. Ejecuta los siguientes comandos en orden:

   ```
   # Crear el entorno virtual con nombre específico
   uv venv browser_use_ve --python 3.11

   # Activar el entorno virtual
   browser_use_ve\Scripts\activate
   ```
   Verás que el prompt cambia para mostrar `(browser_use_ve)` al inicio

4. Para desactivar el entorno virtual cuando termines, escribe:
   ```
   deactivate
   ```

## Instalación de Dependencias

1. Asegúrate de que el entorno virtual está activado (deberías ver `(browser_use_ve)` al inicio del prompt)
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
   OPENAI_API_KEY=<tu_clave_api_aquí>
   ```
   Reemplaza `<tu_clave_api_aquí>` con tu clave de API de OpenAI

## Ejecución del Programa

1. Asegúrate de que el entorno virtual está activado
2. Ejecuta:
   ```
   uv run agent.py
   ```

## Solución de Problemas Comunes

- **Error al instalar uv**: 
  - Intenta ejecutar el comando de instalación nuevamente
  - Asegúrate de haber reiniciado el Símbolo del sistema después de la instalación
  - Verifica que tienes conexión a internet

- **Error al activar el entorno virtual**:
  - Asegúrate de estar en el directorio correcto
  - Verifica que el directorio `browser_use_ve` existe
  - Comprueba que Python 3.11 está instalado correctamente

- **Error al instalar dependencias**:
  - Verifica que el entorno virtual está activado
  - Asegúrate de tener conexión a internet

- **Error al ejecutar el programa**:
  - Verifica que el archivo `.env` existe y contiene la clave API correcta
  - Asegúrate de que todas las dependencias están instaladas

## Para Detener el Programa

Presiona `Ctrl + C` en la terminal donde se está ejecutando el programa.
