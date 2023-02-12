FROM python:3-slim

COPY ./requirements.txt /srv/static_dataprovider/requirements.txt

RUN cd /srv/static_dataprovider && pip3 install --no-cache-dir -r requirements.txt

COPY . /srv/static_dataprovider

WORKDIR /srv/static_dataprovider

CMD ["python3","app.py","remote", "init"]
