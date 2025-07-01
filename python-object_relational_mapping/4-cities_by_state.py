#!/usr/bin/python3
"""This script connects to the hbtn_0e_4_usa database and lists all cities
along with their corresponding state names, 
sorted by city id in ascending order."""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name \
                   FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
