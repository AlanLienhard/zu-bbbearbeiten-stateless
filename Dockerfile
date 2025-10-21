# 1) Basisimage
FROM python:3.11-slim

# 2) Arbeitsverzeichnis
WORKDIR /app

# 3) System-Dependencies (optional, hier minimal)
RUN pip install --upgrade pip

# 4) Projektdateien kopieren
COPY requirements.txt ./
RUN pip install -r requirements.txt || true

COPY . .

# 5) Flask für Containerbetrieb
ENV FLASK_APP=main.py
ENV PYTHONUNBUFFERED=1

# 6) Port (innen)
EXPOSE 5000

# 7) Startkommando
CMD ["python", "main.py"]
