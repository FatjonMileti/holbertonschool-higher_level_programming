#!/usr/bin/python3
''' *** *** '''
import MySQLdb
from sys import argv


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("""
            SELECT cities.name FROM cities, states
            WHERE states.id = cities.state_id AND states.name = %s
            ORDER BY cities.id
        """, (argv[4], ))
    rows = cur.fetchall()

    print(", ".join([row[0] for row in rows]))
