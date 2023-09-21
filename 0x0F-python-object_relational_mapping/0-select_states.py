#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the script is run as the main program
    Mydb = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )
    cursor = Mydb.cursor()
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    Mydb.close()
