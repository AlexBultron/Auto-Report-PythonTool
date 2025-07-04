from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Report(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    value = Column(Float)
