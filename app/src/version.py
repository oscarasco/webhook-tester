from pydantic import BaseModel


class Version(BaseModel):

    version: str = "v.0.0.1"


webhook_tester_version = Version()
