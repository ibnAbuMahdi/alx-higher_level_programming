#!/usr/bin/python3
""" Start link class to table in database """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if len(sys.argv) == 4:
    if __name__ == "__main__":
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(sys.argv[1], sys.argv[2],
                                       sys.argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)

        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
        for city_ins in instance.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")
#
#       query = session.query(State).order_by(State.id)
#        for state in query.all():
#            print("{}: {}".format(state.id, state.name))
#            for city in state.cities:
#                print("    {}: {}".format(city.id, city.name))
