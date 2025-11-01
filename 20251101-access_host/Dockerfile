FROM debian:trixie-slim

RUN apt-get update && \
    apt-get install -y golang curl iproute2

COPY test.sh /usr/bin/test.sh
