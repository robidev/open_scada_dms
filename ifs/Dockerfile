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
	&& cp build/lib60870.so /usr/local/lib/

COPY ./requirements.txt /srv/ifs/requirements.txt

RUN cd /srv/ifs && pip3 install -r requirements.txt

COPY . /srv/ifs

WORKDIR /srv/ifs

CMD ["python3","app.py","remote"]
