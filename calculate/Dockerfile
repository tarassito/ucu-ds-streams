FROM python:3.8-slim

WORKDIR /app

RUN pip3 install faust

COPY . .

CMD [ "faust", "-A", "app", "worker"]
