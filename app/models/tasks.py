from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    title:Mapped[str] = mapped_column(String)
    status:Mapped[str] = mapped_column(String, default="todo")
    project_id:Mapped[int] = mapped_column(Integer, ForeignKey("projects.id"))
    project: Mapped["Project"] = relationship("Project",back_populates="tasks")
    created_at: Mapped[datetime] = mapped_column(Date, default=datetime.utcnow)

