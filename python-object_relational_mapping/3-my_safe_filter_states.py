#!/usr/bin/python3
"""Display name argument of states table"""
import MySQLdb
import sys


def filter_names_safe():
    
    if len(sys.argv) == 5:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])

        cursor = db.cursor()

        cursor.execute("SELECT * FROM states WHERE BINARY name='{:s}'\
                    ORDER BY id ASC".format(sys.argv[4]))
        rows = cursor.fetchall()
        for i in rows:
            print(i)

        cursor.close()
        db.close()
    else:
        return

if __name__ == "__main__":
    filter_names_safe()