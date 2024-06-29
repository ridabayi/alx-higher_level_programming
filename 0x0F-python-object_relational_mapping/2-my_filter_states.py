#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username> <password> <database_name> <state_name>")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL Database: {e}")
        sys.exit(1)

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query
    query = f"SELECT * FROM states WHERE name = '{state_name}' ORDER BY id ASC"

    try:
        # Execute the SQL command
        cursor.execute(query)
        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error executing MySQL query: {e}")

    # Disconnect from server
    db.close()
