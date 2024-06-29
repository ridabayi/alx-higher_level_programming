#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)
    cursor = db.cursor()

    # Construct SQL query with format to avoid SQL injection risks
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    # Execute SQL query
    cursor.execute(query)

    # Fetch all rows matching the query
    rows = cursor.fetchall()

    # Print results as specified
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
