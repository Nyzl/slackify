FROM python:3.7

LABEL version="2.0"
LABEL maintainer="Ian Ansell"

RUN pip install --upgrade pip

COPY . /slackify
WORKDIR /slackify

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod 444 src/*.py
RUN chmod 444 requirements.txt

ENV PORT=8080
ENV GUNICORN_CMD_ARGS="--timeout 600 --graceful-timeout 300 --workers 1 --chdir=./src/"

EXPOSE 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 src.wsgi:app