FROM python:3.11.2

WORKDIR /app

COPY ./requirements.txt /app

RUN apt update && \
    apt upgrade -y && \
    pip install -r requirements.txt

COPY . /app