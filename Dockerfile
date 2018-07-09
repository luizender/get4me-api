FROM alpine:3.7
MAINTAINER Luiz Gustavo Ender <luiz.ender@gmail.com>
RUN apk add --no-cache --update python3 python3-dev gcc libc-dev \
    mariadb-client mariadb-client-libs mariadb-dev
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install --no-cache-dir -Ur requirements.txt && \
    rm -r /root/.cache
COPY ./wait-for-database.sh /