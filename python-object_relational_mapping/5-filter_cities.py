#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    st = sys.argv[4].split('\'')
    cursor = db.cursor()
    cursor.execute("""
                SELECT cities.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                WHERE states.name='{}'
                ORDER BY cities.id ASC
                """.format(st[0]))

    query_rows = cursor.fetchall()
    for row in range(0, len(query_rows)):
        if row < (len(query_rows) - 1):
            print(query_rows[row][0], end=", ")
        else:
            print(query_rows[row][0], end="")
    print()
    cursor.close()
