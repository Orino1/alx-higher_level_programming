#!/usr/bin/python3
"""
Retrieve and print a list of states from a MySQL database.
Usage: script.py <username> <password> <database_name> <state_name_searched>
Also: its safe from MySQL injections.
"""
import sys
import MySQLdb


def main():
    """
    Connect to a MySQL database and print a the id and name
    of a state that matche the searched name.
    Usage: script.py <username> <password> <database_name>
    <state_name_searched>
    """
    connection = MySQLdb.connect(
                user=sys.argv[1],
                passwd=sys.argv[2],
                host='localhost',
                port=3306,
                db=sys.argv[3]
            )
    cursor = connection.cursor()
    query = f"""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id;
        """
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    main()
