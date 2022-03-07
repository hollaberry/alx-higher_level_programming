#!/usr/bin/python3
"""list all the cities of a state taken
as user input argument from hbtn_0e_4_usa
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
    newcmd = """SELECT cities.name
             FROM states
             INNER JOIN cities ON states.id = cities.state_id
             WHERE states.name=%s
             ORDER BY cities.id ASC"""
    cur.execute(newcmd, (sys.argv[4],))
    allcities = cur.fetchall()
    
    print(", ".join([city[0] for city in allcities]))

    cur.close()
    db.close()
