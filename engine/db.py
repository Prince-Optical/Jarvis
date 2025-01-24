import csv
import sqlite3

conn = sqlite3.connect("friday.db")
cursor = conn.cursor()
# to build table in data base 
query = "CREATE TABLE IF NOT EXISTS SYS_COMMAND(id integer primary key, name VARCHAR(100), path VARCHAR(100))"
cursor.execute(query)
# insert into table SYS_COMMAND 
#query = "INSERT INTO SYS_COMMAND VALUES(null,'google chrome','C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')"
#cursor.execute(query)
#conn.commit()

# Web command 
query = "CREATE TABLE IF NOT EXISTS WEB_COMMAND (id integer primary key, name VARCHAR(100), url VARCHAR(100))"
cursor.execute(query)
# INSERT IN WEB  COMMAND 
#query = "INSERT INTO WEB_COMMAND VALUES(null,'wikipedia','https://www.wikipedia.org/')"
#cursor.execute(query)
#conn.commit()

# Create a table with the desired columns
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
#desired_columns_indices = [0, 30]

# Read data from CSV and insert into SQLite table for the desired columns
#with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
    #csvreader = csv.reader(csvfile)
    #for row in csvreader:
        #selected_data = [row[i] for i in desired_columns_indices]
        #cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# Commit changes and close connection
#conn.commit()
#conn.close()
# Single contact 
#query = "INSERT INTO contacts VALUES (null,'piyush soni', '8955019297','null')"
#cursor.execute(query)
#conn.commit()

#searching name in contact 
#query = 'ghanshyam'
#query = query.strip().lower()

#cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
#results = cursor.fetchall()
#print(results[0][0])
