#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    if len(sys.argv) == 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                               format(sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)

        Base.metadata.create_all(engine)
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        upd = 'New Mexico'

        try:

            query = session.query(State).filter(State.id == 2).first()
            query.name = upd
            session.commit()

        except SQLAlchemyError as e:
            print(e)
        finally:
            session.close()