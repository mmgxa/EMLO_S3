FROM python:3.8-slim-buster

MAINTAINER MMG

WORKDIR /app

COPY './requirements.txt' .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "app.py"]
