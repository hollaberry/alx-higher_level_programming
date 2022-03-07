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
    newcmd = """SELECT id, name
            FROM states
            WHERE name=%s
            ORDER BY id ASC;"""
    cur.execute(newcmd, (sys.arg[4],))
    stateswithN = cur.fetchall()

    for state in stateswithN:
        print(state)

    cur.close()
    db.close()
