#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":

    if len(sys.argv) == 5:
        db = MySQLdb.connect(host="localhost", port=3306,
                            user=sys.argv[1],
                            passwd=sys.argv[2],
                            db=sys.argv[3])

        cursor = db.cursor()
        cursor.execute("""
                    SELECT *
                    FROM states
                    WHERE BINARY name='{:s}'
                    ORDER BY id ASC
                    """.format(sys.argv[4]))

        rows = cursor.fetchall()
        for row in rows:
            if row[1] == sys.argv[4]:
                print(row)

        cursor.close()
        db.close()