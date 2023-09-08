"""
This is a SQL query using python script.
"""
import sys
import MySQLdb


def list_states(username, password, database_name):
    """
    Here's the logic to get arguments from the command line.
    """
    try:
        # Connect to the MySQL server on localhost at port 3306
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Retrieve all states from the 'states' table and order by 'id' in ascending order
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch and print the results
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Don't forget to commit changes and close the cursor and connection
        db.commit()
        cursor.close()
        db.close()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        list_states(username, password, database_name)
