FROM python:3-slim

COPY ./requirements.txt /srv/client/requirements.txt

RUN cd /srv/client && pip3 install --no-cache-dir -r requirements.txt

COPY . /srv/client

WORKDIR /srv/client

EXPOSE 5000

CMD ["python3","app.py","remote"]
