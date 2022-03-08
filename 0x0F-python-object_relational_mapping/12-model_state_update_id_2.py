#!/usr/bin/python3
"""list all States objects from the
database hbtn_0e_6_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.sql.expression import update

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]))
    result = session.query(State).filter(State.id == 2)
    result.update({"name": ("New Mexico")})

    session.commit()
