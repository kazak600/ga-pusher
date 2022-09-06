FROM python:3.9

COPY . /backend
WORKDIR /backend

RUN pip install -r /backend/requirements.txt