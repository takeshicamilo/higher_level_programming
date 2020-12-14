#!/usr/bin/python3

import sys
import MySQLdb

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
x = 0

cur.execute("SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id AND states.name = '{}'".format(sys.argv[4]))
ll = [x[0] for x in cur.fetchall()]
together = ", ".join(ll)
print(together)