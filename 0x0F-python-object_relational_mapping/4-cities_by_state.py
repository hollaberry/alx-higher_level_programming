#!/usr/bin/python3
"""List all states from a given db sorted in
ascending order by id, Username, password,
and database names are given as user args
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    newcmd = """SELECT cities.id, cities.name, states.name
            FROM states
            INNER JOIN cities ON states.id = cities.state_id
            ORDER BY cities.id ASC;"""
    cur.execute(newcmd)
    allcities = cur.fetchall()
    for city in allcities:
        print(state)

    cur.close()
    db.close()
