#!/usr/bin/python3
"""
Retrieve and print a list of states from a MySQL database.
Usage: script.py <username> <password> <database_name>
"""
import sys
import MySQLdb


def main():
    """
    Connect to a MySQL database and print a list of states that
    starts with with N (upper N) from the database hbtn_0e_0_usa.
    Usage: script.py <username> <password> <database_name>
    """
    connection = MySQLdb.connect(
                user=sys.argv[1],
                passwd=sys.argv[2],
                host='localhost',
                port=3306,
                db=sys.argv[3]
            )

    cursor = connection.cursor()
    query = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    main()
