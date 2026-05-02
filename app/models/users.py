from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import List
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email:Mapped[str] = mapped_column(String, unique=True)
    hashed_password:Mapped[str] = mapped_column(String)
    role:Mapped[str] = mapped_column(String, default="member")
    created_at:Mapped[datetime] = mapped_column(Date, default=datetime.utcnow)
    projects:Mapped[List["Project"]] = relationship("Project",back_populates="owner")


