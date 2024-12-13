from app.backend.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from app.models import *

class Task(Base):
    __tablename__ = "task"
    __table_args__ = {"keep_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True, index=True)
    slug = Column(String, unique=True, index=True)
    user = relationship("Users", back_populates="task")


print(CreateTable(Task.__table__))
