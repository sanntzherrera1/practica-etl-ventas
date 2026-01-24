#El slim es una version ligera con menos librerias

FROM python:3.14-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Esto copia el codigo fuente
COPY . .

# Esto le dice que archivo ejecutar cuando se inicie el contenedor
CMD ["python", "src/main.py"]
