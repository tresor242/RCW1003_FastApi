FROM python:3.10-slim

WORKDIR /app

# Copier les deux dossiers (FastAPI + Dash)
COPY ./fastApi_app ./fastApi_app
COPY ./dash_app ./dash_app
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Aller dans le bon dossier à l'exécution
WORKDIR /app/fastApi_app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
