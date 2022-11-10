#!/usr/bin/python3
''' *** *** '''
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import sys


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
                           f"@localhost/{sys.argv[3]}")
    with Session(engine) as session:
        result = session.query(State).first()
        if result:
            print(f"{result.id}: {result.name}")
        else:
            print("Nothing")
