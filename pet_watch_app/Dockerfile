# syntax=docker/dockerfile:1

FROM python:3.10.8-slim-buster

WORKDIR /pet_watch_app

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .