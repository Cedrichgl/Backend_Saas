import datetime
from pydantic import BaseModel, ConfigDict


class TaskCreate(BaseModel):
    title:  str
    project_id: int

class TaskOut(BaseModel):
    id: int
    title: str
    status: str
    project_id: int
    created_at: datetime.datetime

    model_config= ConfigDict(from_attributes=True)

