#!/usr/bin/python3
"""
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycur = db.cursor()
    arg = sys.argv[4]
    mycur.execute("""SELECT cities.name FROM cities INNER JOIN states ON
                cities.state_id=states.id WHERE states.name=%s""", (arg,))
    states = mycur.fetchall()
    for state in states:
        print(state)
    mycur.close()
    db.close()
