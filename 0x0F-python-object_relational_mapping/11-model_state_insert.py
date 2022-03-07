#!/usr/bin/python3
"""list State object with 'name' passed
as arg from db 'hbtn_0e_6_usa'
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    c1 = State(name = 'Louisiana')
    session.add(c1)
    session.commit()

    print(state.id)
