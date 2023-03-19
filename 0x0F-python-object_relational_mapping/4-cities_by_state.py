#!/usr/bin/python3
""" 0-select_states """
import MySQLdb as msql
import sys


if len(sys.argv) == 4:
    db = msql.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON states.id = cities.state_id ORDER BY cities.id")
    
    for row in cur.fetchall():
        print(row)
    
    cur.close()
