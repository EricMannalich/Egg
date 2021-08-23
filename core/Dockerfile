FROM python:3.9.5

ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
RUN mkdir /code/
WORKDIR /code

COPY apps /code/
COPY config /code/
COPY requirements.txt /code/
COPY core /code/
COPY manage.py /code/

#Para poder instalar sycopg2 en python:alpine es necesario: 
#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN python -m pip install -r requirements.txt