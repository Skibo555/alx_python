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

    if len(args) <= 4:
        return
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]

    try:

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=arg1,
            passwd=arg2,
            db=arg3
        )
        db_cursor = db.cursor()
        db_cursor.execute("SELECT states")
        db_cursor.execute("ORDER BY states.id ASC")
        result = db_cursor.fetchall()
        for row in result:
            print(row)
        db.commit()
        db_cursor.close()
        db.close()

    except Exception as q:
        return ("{}, shey you no see ni?".format(q))


if __name__ == '__main__':
    sql()
