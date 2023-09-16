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
    state_name = sys.argv[4]
    cursor = connection.cursor()
    query = f"""
        SELECT cities.name
        FROM cities
        JOIN states ON states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
        """
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()
    city_names = ""
    for state in states:
        if city_names:
            city_names += ", "
        city_names += state[0]
    print(city_names)


if __name__ == "__main__":
    main()
