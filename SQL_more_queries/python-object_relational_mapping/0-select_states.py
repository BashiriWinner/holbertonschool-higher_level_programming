#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY ASC")

    rows = cusrsor.fetchall()

    for row in rows:
        print(row)

        cursor.close()
        db.close

