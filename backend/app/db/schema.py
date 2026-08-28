from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.database import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = Base.metadata

class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True)
    title = Column(String(40), unique=False)
    description = Column(String(200), unique=False)
    due_datetime = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)
    done = Column(Boolean, default=False)
    active = Column(Boolean, default=True)