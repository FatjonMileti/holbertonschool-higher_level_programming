#!/usr/bin/python3
''' *** *** '''
from model_state import State
from model_city import City
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import sys


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
                           f"@localhost/{sys.argv[3]}")
    with Session(engine) as session:
        results = session.query(State, City).\
                filter(State.id == City.state_id).order_by(City.id)
        for state, city in results:
            print(f"{state.name}: ({city.id}) {city.name}")
