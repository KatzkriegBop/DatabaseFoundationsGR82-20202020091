FROM python:3.11-slim

WORKDIR /SteamApp

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /SteamApp

# Establecer PYTHONPATH
ENV PYTHONPATH=/SteamApp

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]