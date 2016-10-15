FROM python:2.7-slim

# ENV OPENSSL_VERSION 1.0.1q

RUN apt-get update && apt-get install --no-install-recommends -y \
    git curl build-essential && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /build 

RUN cd /build && virtualenv ./env && . ./env/bin/activate

WORKDIR /build

# COPY run.sh /run.sh

# ENTRYPOINT ["/run.sh"]

