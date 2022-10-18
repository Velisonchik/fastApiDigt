FROM python:slim

WORKDIR /fastapi-digt

ADD main.py ./server/
ADD config.py ./server/

RUN pip3 install fastapi uvicorn

