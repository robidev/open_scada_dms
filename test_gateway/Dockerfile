FROM debian:stable-20211115-slim

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
              git \
              build-essential \  
              python3 \
              python3-pip \
        && rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=

RUN git clone -b master https://github.com/mz-automation/lib60870.git /tmp/lib60870

RUN cd /tmp/lib60870/lib60870-C && make dynlib \
	&& cp build/liblib60870.so /usr/local/lib/lib60870.so


COPY . /srv/test_gateway

WORKDIR /srv/test_gateway

EXPOSE 2404

CMD ["python3","app.py","config.remote.ini"]

