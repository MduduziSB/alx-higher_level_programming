#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycur = db.cursor()
    arg = sys.argv[4]
    mycur.execute("SELECT * FROM states WHERE name LIKE %s", (arg, ))
    states = mycur.fetchall()
    for state in states:
        print(state)
    mycur.close()
    db.close()
