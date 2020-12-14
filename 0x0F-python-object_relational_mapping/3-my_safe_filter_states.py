#!/usr/bin/python3
"""
all states in orderfrom the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC".format(sys.argv[4]))

    for state in cur.fetchall():
        print(state)
    cursor.close()
    db.close()