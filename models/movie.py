from Config.database import Base
from sqlalchemy import Column, Integer, String, Float


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Integer)
    category = Column(String(50))