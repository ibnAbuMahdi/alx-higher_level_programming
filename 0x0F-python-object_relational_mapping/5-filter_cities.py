#!/usr/bin/python3
""" 0-select_states """
import MySQLdb as msql
import sys


if len(sys.argv) == 5:
    db = msql.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    
    cur = db.cursor()
    search = sys.argv[4].split("'")[0]
    cur.execute("SELECT cities.name FROM cities JOIN states ON states.id = cities.state_id WHERE states.name LIKE %s", (search,))
    
    cnt = cur.rowcount
    for row in cur.fetchall():
        if cnt != cur.rowcount:
            print(", " + row[0], end="")
        else:
            print(row[0], end="")
        cnt -= 1
    
    print()
    cur.close()
