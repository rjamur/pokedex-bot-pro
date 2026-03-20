# Usa a imagem oficial e enxuta do Python 3.12
FROM python:3.12-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Avisa o Python para não prender os prints no buffer! (A Mágica)
ENV PYTHONUNBUFFERED=1

# Copia primeiro o requirements para otimizar o cache do Docker
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do projeto
COPY . .

# Comando que inicia o bot
CMD ["python", "main.py"]
