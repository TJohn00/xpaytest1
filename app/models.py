from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.db import engine
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True)
    password = Column(String)
    profile_picture_id = Column(String, nullable=True)

Base.metadata.create_all(bind=engine)