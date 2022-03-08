#!/usr/bin/python3
"""adds the State object "California"
with the city "SanFrancisco"
to the atabase hbtn_0e_100_usa
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
    new_city = City(name='San Francisco')
    new = State(name='California')
    new.cities.append(new_city)
    session.add_all([new, new_city])
    session.commit()
    session.close()
