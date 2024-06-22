#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Arguments: mysql_username, mysql_password, database_name
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server running on localhost at port 3306
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=mysql_username,
                           passwd=mysql_password,
                           db=database_name)

    # Create a cursor object using cursor() method
    cur = conn.cursor()

    # Execute a query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows using fetchall() method
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()
