FROM alpine:3.7
MAINTAINER Luiz Gustavo Ender <luiz.ender@gmail.com>
RUN apk add --no-cache --update python3 python3-dev gcc libc-dev make \
    mariadb-client mariadb-client-libs mariadb-dev