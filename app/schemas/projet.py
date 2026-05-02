import datetime
from pydantic import BaseModel, ConfigDict

class ProjectCreate(BaseModel):
    name: str
    description: str


class ProjectOut(BaseModel):
    id: int
    name: str
    description: str
    owner_id: int
    created_at: datetime.datetime

    model_config = ConfigDict(from_attributes=True)

