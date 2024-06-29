#!/usr/bin/python3
"""
This script filters states by user input from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials, database name, and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    # Create a cursor object
    cursor = db.cursor()

    # Prepare the SQL query using format to insert user input safely
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    
    # Execute SQL query
    cursor.execute(query)

    # Fetch all the rows from the executed query
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
