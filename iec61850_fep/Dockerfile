FROM debian:stable-20211115-slim

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
              git \
              build-essential \  
              python3 \
              python3-pip \
        && rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=

RUN git clone -b v1.4 https://github.com/mz-automation/libiec61850.git /tmp/libiec61850

RUN cd /tmp/libiec61850 && make dynlib \
	&& cp build/libiec61850.so /usr/local/lib/

COPY ./requirements.txt /srv/iec61850_fep/requirements.txt

RUN cd /srv/iec61850_fep && pip3 install --break-system-packages -r requirements.txt

COPY . /srv/iec61850_fep

WORKDIR /srv/iec61850_fep

CMD ["python3","app.py","remote"]
