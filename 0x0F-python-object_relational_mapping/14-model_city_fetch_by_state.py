#!/usr/bin/python3
"""list all City objects from the
database hbtn_0e_14_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State, City).filter(State.id == City.state_id)
    for row in result:
        print("{}: ({:d}) {}".format(row.State.name,\
                                     row.City.id, row.City.name))
