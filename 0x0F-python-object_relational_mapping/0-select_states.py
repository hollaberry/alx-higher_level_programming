#!/usr/bin/python3
"""List all states from a given db sorted in ascending order by id, Username, password, and database names are given as user args
"""
if __name__ == "__main__":

   import MySQLdb
   import sys

   db = MySQLdb.connect(host='localhost',
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3])
   
   cur = db.cursor()
   cur.execute("SELECT id, name FROM states ORDER BY id ASC")
   all_states = cur.fetchall()

   for state in all_states:
      print(state)
