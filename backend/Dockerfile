# Dockerfile-bakend

# Imagem base
FROM python:3.9

# Definir o diretorio de trabalho no container
WORKDIR /app

# Copiar os arquivos de dependencias e instalar
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiar o restante dos arquivos do projeto
COPY . /app

# Comando para executar a aplicacao
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]