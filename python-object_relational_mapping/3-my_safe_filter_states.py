"""
This is a module that gets fucks done on a SQL server.
"""

import sys
import MySQLdb


def sql():
    if len(sys.argv) != 5:
        exit
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        search = sys.argv[4].format()

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )
    db_cur = connection.cursor()

    sql_query = ("SELECT * FROM states WHERE name COLLATE utf8mb4_bin LIKE %s \
            ORDER BY id ASC")
    db_cur.execute(sql_query, ('%' + search + '%',))

    results = db_cur.fetchall()
    for row in results:
        print(row)

    connection.close()


if __name__ == '__main__':
    sql()
