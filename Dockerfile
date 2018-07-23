FROM alpine:3.8
MAINTAINER Luiz Gustavo Ender <luiz.ender@gmail.com>
WORKDIR /build
ENV CLOUD_SDK_VERSION 209.0.0
ENV PATH /build/google-cloud-sdk/bin:$PATH
ADD ./api/requirements.txt /build/
RUN apk add --no-cache --update python python3 postgresql-client postgresql-libs make curl gcc python3-dev musl-dev postgresql-dev && \
    curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    ln -s /lib /lib64 && \
    curl -o /build/google-cloud-sdk/bin/cloud_sql_proxy https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 && \
    chmod +x /build/google-cloud-sdk/bin/cloud_sql_proxy && \
    pip3 install -r requirements.txt --no-cache-dir