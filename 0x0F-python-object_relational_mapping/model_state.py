#!/usr/bin/python3
""" model_state class """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import relationship
from sqlalchemy.engine.url import URL
Base = declarative_base()
db_url = {'drivername': 'mysql',
          'username': 'root',
          'password': 'root',
          'host': 'localhost',
          'port': 3306}
engine = create_engine('mysql+mysqldb://root:root@localhost:\
                       3306/hbtn_0e_6_usa', pool_pre_ping=True)

if __name__ == "__main__":
    class State(Base):
        """ State class that inherits Base """

        __tablename__ = 'states'
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)


    Base.metadata.create_all(bind=engine)
