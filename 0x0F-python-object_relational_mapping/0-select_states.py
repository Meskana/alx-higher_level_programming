#!/usr/bin/python3

"""
a script that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb
if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306, user =sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    print_st = cur.fetchall()
    for st in print_st:
        print(st)
    conn.close()
    cur.close()
