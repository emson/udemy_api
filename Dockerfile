FROM python:2.7-slim

# ENV OPENSSL_VERSION 1.0.1q

RUN apt-get update && apt-get install --no-install-recommends -y \
    git curl build-essential zip && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /build

RUN pip install virtualenv

RUN cd /build && virtualenv ./env && . ./env/bin/activate

WORKDIR /build

CMD make clean build package

# COPY run.sh /run.sh

# ENTRYPOINT ["/run.sh"]

