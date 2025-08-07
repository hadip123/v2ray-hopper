FROM docker.arvancloud.ir/alpine:3.22

RUN echo "http://repo.iut.ac.ir/repo/alpine/v3.22/main" > /etc/apk/repositories
RUN echo "http://repo.iut.ac.ir/repo/alpine/v3.22/community" >> /etc/apk/repositories

RUN apk add zsh v2ray npm nodejs python3 py3-pip py3-dotenv

WORKDIR /venv

RUN python3 -m venv env

RUN . env/bin/activate && pip3 install requests "requests[socks]" dotenv

WORKDIR /app

RUN mkdir -p /app/tester/wcp /app/tester/configs
