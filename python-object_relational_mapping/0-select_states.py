"""
This is a SQL query using python script.
"""
import sys
import MySQLdb


def sql():
    """
    Here's the logic to get arguments from the command line.
    """
    args = sys.argv[1:]

    if len(args) <= 3:
        return
    arg1 = sys.argv[0]
    arg2 = sys.argv[1]
    arg3 = sys.argv[2]
    db = MySQLdb.connect(
        host="localhost",
        user=arg1,
        passwd=arg2,
        db=arg3
    )
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states")
    db_cursor.execute("ORDER BY states.id [ASC|DESC]")


if __name__ == '__main__':
    sql()
