import datetime
import uuid
from typing import List

from pydantic import RootModel, Field

from api.schema.base import BaseApiSchema


class Path(BaseApiSchema):
    path: uuid.UUID
    total_message: int
    last_message_at: datetime.datetime


class Paths(RootModel):
    root: List[Path] = Field(default_factory=list)
