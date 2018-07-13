FROM alpine:3.8
MAINTAINER Luiz Gustavo Ender <luiz.ender@gmail.com>
WORKDIR /build
ADD requirements.txt /build/
RUN apk add --no-cache --update python3 postgresql-client postgresql-libs make && \
    apk add --no-cache --update --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
    pip3 install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps