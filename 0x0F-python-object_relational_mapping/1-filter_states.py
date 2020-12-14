#!/usr/bin/python3
#print only states with N

import MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()

cur.execute("SELECT * FROM states WHERE name REGEXP '^[n]'")

for state in cur.fetchall():
        print(state)