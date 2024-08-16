# Use uma imagem base do Python
FROM python:3.12-slim

# Instale as dependências do PostgreSQL e outras necessárias
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de dependências
COPY requirements.txt requirements.txt

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Defina a variável de ambiente FLASK_APP
ENV FLASK_APP=app

# Execute o Flask
CMD ["flask", "run", "--host=0.0.0.0"]
