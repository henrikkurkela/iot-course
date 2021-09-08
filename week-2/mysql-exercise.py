# Learn how to
# - Create database
# - Create table
# - Insert record
# - Select data
# using Python.

import sys
import mysql.connector

db_user = ''
db_passwd = ''

# Get credentials from CLI arguments
if (len(sys.argv) < 3):
    print('Give MySQL credentials as command line arguments: program.py <username> <password>')
    exit()
else:
    db_user = sys.argv[1]
    db_passwd = sys.argv[2]

# Connect
db = mysql.connector.connect(
    host='localhost',
    user=db_user,
    password=db_passwd
)

# Create and use database if it doesn't exist
db._execute_query('CREATE DATABASE IF NOT EXISTS python')
db._execute_query('USE python')

# Create table if it doesn't exist
db._execute_query(
    'CREATE TABLE IF NOT EXISTS hamburgers (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(255))')

# Insert records
db._execute_query('INSERT INTO hamburgers (name) VALUES ("Cheeseburger")')
db._execute_query('INSERT INTO hamburgers (name) VALUES ("Big Mac")')
db.commit()

# Select records
db_cursor = db.cursor()

db_cursor.execute("SELECT * FROM hamburgers")

db_result = db_cursor.fetchall()

for i in db_result:
    print(i)

# Clean up
db._execute_query('DELETE FROM hamburgers')
db.commit()
