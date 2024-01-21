from fastapi import FastAPI

from api.v1.message import router as message_router

app = FastAPI(
    title="Webhook Tester",
    version='0.0.1',
    contact={
        "name": "Enrico",
        "email": "enricovela@gmail.com"
    },
)

app.include_router(
    message_router,
    prefix="/v1",
    tags=["Message"],
)
