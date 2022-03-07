#!/usr/bin/python3
"""list all States objects from the
database hbtn_0e_6_usa
"""

if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State


    engine = create_engine('mysql+mysqldb://{}:{}@localhost:/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).all()

    for row in result:
        print("{:d}: {}".format(row.id, row.name))
    session.close()
