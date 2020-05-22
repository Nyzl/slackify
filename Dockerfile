FROM python:3.7

LABEL version="1.0"
LABEL maintainer="Ian Ansell"

RUN pip install --upgrade pip

COPY . /slackify
WORKDIR /slackify

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod 444 src/*.py
RUN chmod 444 requirements.txt

ENV PORT 8080

ENV GUNICORN_CMD_ARGS="--timeout 600 --graceful-timeout 300 --workers 2 --chdir=./src/"


CMD ["gunicorn", "app:app"]