#!/usr/bin/python3
"""List from table state"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name = argv[4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8"
    )
    cursor = db.cursor()
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s;
    """
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))
    cursor.close()
    db.close()
