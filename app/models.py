from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(255))
    preferences = relationship("Preference", back_populates="user")

class Preference(Base):
    __tablename__ = "preferences"
    id = Column(Integer, primary_key=True)
    emojis = Column(Text)
    movie_title = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="preferences")
