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
        search = 'Louisiana'

        lui = State(name=search)
        try:
            session.add(lui)
            session.commit()

            query = session.query(State).filter(State.name == search)

            row = query.scalar()
            if row:
                print(row.id)
            else:
                print("Not found")

        except SQLAlchemyError as e:
            print(e)
        finally:
            session.close()
