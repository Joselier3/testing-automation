# Quickstart

1. Instalar el manejador de paquetes de Python, **uv**,

Linux
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Crear el entorno virtual con uv utilizando Python 3.11, y requirements.txt
```
uv venv --python 3.11

source .venv/bin/activate # linux
.venv\Scripts\activate # Windows

uv pip install -r requirements.txt
```

3. Instalar `playwright` (Paquete para acceder a navegadores, en este caso, chromium)
```
uvx playwright install
```

4. Añade una llave de API para OpenAI a un archivo `.env`
```
OPENAI_API_KEY=<your_api_key>
```

5. Ejecuta `agent.py`
```
uv run agent.py
```
