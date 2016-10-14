FROM python:2.7-slim

# ENV OPENSSL_VERSION 1.0.1q

RUN apt-get update && apt-get install --no-install-recommends -y \
    git  curl && rm -rf /var/lib/apt/lists/*

RUN pip install lambda-uploader \
    && mkdir /data

RUN virtualenv /venv && . /venv/bin/activate \
    && mkdir -p /var/task && cd /var/task \
    && cd ..

WORKDIR /data

COPY run.sh /run.sh

ENTRYPOINT ["/run.sh"]

