from fastapi import FastAPI

from api.v1.message import router as message_router


from fastapi.middleware.cors import CORSMiddleware

from version import webhook_tester_version

origins = ["*"]

app = FastAPI(
    title="Webhook Tester",
    version=webhook_tester_version.version,
    contact={
        "name": "Enrico",
        "email": "enricovela@gmail.com"
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    message_router,
    prefix="/api/v1",
    tags=["Message"],
)

