#!/usr/bin/python3
""" 0-select_states """
import MySQLdb as msql
import sys

if __name__ == "__main__":
    if len(sys.argv) == 5:
        db = msql.connect(host='localhost', port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])

        cur = db.cursor()
        search = sys.argv[4].split("'")[0]
        cur.execute("SELECT * FROM states WHERE name LIKE %s", (search,))
        for row in cur.fetchall():
            print(row)

        cur.close()
