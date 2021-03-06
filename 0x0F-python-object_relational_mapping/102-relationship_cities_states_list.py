#!/usr/bin/python3
"""lists all State objeccts, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.schema import Table

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(City).order_by(City.id).all():
    for city in result:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
