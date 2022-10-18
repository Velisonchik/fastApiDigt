FROM python:slim

WORKDIR /fastapi-digt

COPY ./app ./app

RUN pip3 install fastapi uvicorn

CMD ["python","./app/main.py"]