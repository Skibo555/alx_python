"""
This is a script thaat queries the database and it's a SQL injection free!
"""

import sys
import MySQLdb


def injection_free():
    if len(sys.argv) != 5:
        exit
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    obj = db.cursor()

    query = "SELECT * cities"
    result = obj.execute(query, "FORM", state_name)

    db.close()
    for row in result:
        print(row)


if __name__ == '__main__':
    injection_free()
