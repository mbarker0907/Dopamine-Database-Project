import sqlite3

# Connect to the database
conn = sqlite3.connect('dopamine.db')
cursor = conn.cursor()

# Run a query
cursor.execute('SELECT * FROM Activities ORDER BY dopamine_max DESC')
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the connection
conn.close()