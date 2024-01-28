FROM node:18.18 as node
WORKDIR /app
COPY ./frontend/ .
RUN npm install
RUN npm run build-prod


FROM mongo:6.0.13-jammy  as base

RUN apt-get update && \
    apt-get install -y python3 python3-pip nginx

COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app
COPY ./app/src/ /app

FROM base as test

WORKDIR /test
COPY ./app/test/ .
RUN pip3 install -r requirements-test.txt

CMD ["pytest", "-c", "docker-test.ini"]

FROM base as service
COPY --from=node /app/dist/webhook-tester-ui /var/www/html/
COPY ./start.sh /start.sh
CMD ["sh", "/start.sh"]