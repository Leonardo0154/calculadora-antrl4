FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    default-jdk \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY antlr-4.13.2-complete.jar /usr/share/java/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN java -jar /usr/share/java/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -no-listener Calc.g4

# Cambiar el CMD para aceptar argumentos
ENTRYPOINT ["python", "main.py"]
CMD []