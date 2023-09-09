"""
This a SQL query that lists all the cities in the a specified database.
"""

import sys
import MySQLdb


def sql_query():
    if len(sys.argv) != 4:
        exit
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        sql = db.cursor()
        query = ("SELECT cities.id, cities.name, states.name \
                FROM cities, states \
                WHERE states.id = state_id ORDER BY cities.id")

        sql.execute(query)
        result = sql.fetchall()

        for row in result:
            print(row)

        db.close()


if __name__ == '__main__':
    sql_query()
