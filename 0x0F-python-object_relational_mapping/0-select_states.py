#!/usr/bin/python3
""" 0-select_states """
import MySQLdb as msql
import sys



db = msql.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

cur = db.cursor()

cur.execute("SELECT * FROM states")
for row in cur.fetchall():
    print(row)

cur.close()
