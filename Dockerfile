FROM alpine:3.7
MAINTAINER Luiz Gustavo Ender <luiz.ender@gmail.com>
RUN apk add --no-cache --update python3 python3-dev gcc libc-dev make \
    mariadb-client mariadb-client-libs mariadb-dev
WORKDIR /build
ADD requirements.txt /build/
RUN pip3 install --no-cache-dir -r requirements.txt