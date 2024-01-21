FROM mongo:latest

COPY ./start.sh /start.sh
COPY ./requirements.txt requirements.txt

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install -r requirements.txt

WORKDIR /app
COPY ./app/src/ /app

CMD ["sh", "/start.sh"]
