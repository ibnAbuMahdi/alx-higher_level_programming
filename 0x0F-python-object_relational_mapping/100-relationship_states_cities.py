#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
if len(sys.argv) == 4:
    if __name__ == "__main__":
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        search = 'California'
        id_no = None

        Cal = State(name=search)
        try:
            session.add(Cal)
            session.commit()
        except TypeError as e:
            print(e)

        query = session.query(State).filter(State.name == search)
        row = query.all()
        if len(row):
            id_no = row[-1].id
            san = City(name='San Francisco', state_id=id_no)
            try:
                session.add(san)
                session.commit()
            except TypeError as e:
                print(e)
        session.close()
