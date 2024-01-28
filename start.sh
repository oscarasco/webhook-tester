#!/bin/sh

nohup mongod &
nginx -g "daemon off;" &
gunicorn main:app --workers ${WORKERS_NUMBER} \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000