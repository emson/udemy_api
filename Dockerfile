FROM alpine:latest

RUN set -e && \
    set -x && \
    apk add --no-cache --virtual build-deps \
        gcc \
        git \
        python-dev \
        linux-headers \
        curl \
        cmake \
        pkgconf \
        unzip \
        build-base \
        zlib-dev \
        zip && \
    python -m ensurepip && \
    pip --no-cache-dir install --upgrade pip setuptools && \
    mkdir -p /build && \
    pip install virtualenv

WORKDIR /build
VOLUME ["/build"]
CMD ["/bin/sh", "-c", "rm -rf ./env; virtualenv ./env; . ./env/bin/activate; make clean build package"]

