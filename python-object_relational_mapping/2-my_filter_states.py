"""
This is a module that gets fucks done on a SQL server.
"""

import sys
import MySQLdb

if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    search = sys.argv[4]

connection = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=database_name
)
db_cur = connection.cursor()
sql_query = ("SELECT * FROM states WHERE name='search'")
result = sql_query.execute(sql_query)

results = result.fetchall()
for row in results:
    print(row)
connection.close()
