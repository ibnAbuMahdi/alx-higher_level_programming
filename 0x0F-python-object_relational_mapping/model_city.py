#!/usr/bin/python3
""" model_city class """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import relationship
from sqlalchemy.engine.url import URL
from model_state import Base

engine = create_engine('mysql+mysqldb://root:root@localhost:\
                       3306/hbtn_0e_6_usa', pool_pre_ping=True)


class City(Base):
    """ City class that inherits Base """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
