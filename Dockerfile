FROM python:3.7-alpine
MAINTAINER Ankit App ltd.

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .top-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .top-build-deps

RUN mkdir /app
WORKDIR /app
copy ./app /app

RUN adduser -D user
USER user
