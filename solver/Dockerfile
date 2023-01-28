FROM python:3-slim

COPY ./requirements.txt /srv/solver/requirements.txt

RUN cd /srv/solver && pip3 install --no-cache-dir -r requirements.txt

COPY . /srv/solver

WORKDIR /srv/solver

CMD ["python3","app.py","remote"]
