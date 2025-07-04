#!/usr/bin/python3
"""This script connects to the hbtn_0e_0_usa database and lists all states
with a name matching the user-provided argument,
sorted by id in ascending order."""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * \
                    FROM `states` \
                    WHERE BINARY `name` = '{}' \
                    ORDER BY id".format(argv[4]))

    for state in cursor.fetchall():
        print(state)


    cursor.close()
    db.close()
