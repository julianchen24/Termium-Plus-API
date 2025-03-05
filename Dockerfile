FROM python:3.12-alpine

RUN apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    g++ \
    make \
    lapack-dev \
    gfortran \
    bash

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/data

RUN chmod +x ./entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]


