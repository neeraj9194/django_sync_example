FROM python:3.8.5-slim

ENV PYTHONUNBUFFERED 1

EXPOSE 8001
WORKDIR /app

RUN apt update && apt install -y gcc musl-dev libpq-dev

RUN pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system

ADD . /app

CMD gunicorn django_sync_example.wsgi:application --bind 0.0.0.0:8001
