# https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

COPY ./app/requirements.txt /app/base.txt
COPY ./requirements/docker.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app
