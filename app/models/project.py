from datetime import datetime

from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from app.database import Base

class Project(Base):
    __tablename__ = "projects"
    id:Mapped[int]  = mapped_column(Integer, primary_key=True, index=True)
    name:Mapped[str] = mapped_column(String)
    description:Mapped[str] = mapped_column(String)
    owner_id:Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    created_at:Mapped[datetime] = mapped_column(Date, default=datetime.utcnow)

    tasks: Mapped[List["Task"]] = relationship("Task",back_populates="project",cascade="all, delete-orphan")
    owner: Mapped["User"] = relationship("User", back_populates="projects")
