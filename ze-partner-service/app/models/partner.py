from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry

Base = declarative_base()

class Partner(Base):
    __tablename__ = 'partners'
    id = Column(Integer, primary_key=True)
    tradingName = Column(String)
    ownerName = Column(String)
    document = Column(String, unique=True)
    coverageArea = Column(Geometry(geometry_type='MULTIPOLYGON'))
    address = Column(Geometry(geometry_type='POINT'))