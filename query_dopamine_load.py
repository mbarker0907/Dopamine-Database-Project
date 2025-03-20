import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('dopamine.db')

# Define the SQL query
query = """
SELECT au.user_id, au.date, SUM(a.dopamine_max * (au.duration_minutes / 60.0)) AS total_dopamine_load
FROM Activity_Usage au
JOIN Activities a ON au.activity_id = a.activity_id
GROUP BY au.user_id, au.date;
"""

# Execute the query and load results into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Print the results
print("Cumulative Dopamine Load by User and Date:")
print(df)