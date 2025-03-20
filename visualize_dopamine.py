import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the database
conn = sqlite3.connect('dopamine.db')

# Query: Average dopamine by category
query = """
SELECT category, AVG(dopamine_min) AS avg_dopamine_min, AVG(dopamine_max) AS avg_dopamine_max
FROM Activities
GROUP BY category
ORDER BY avg_dopamine_max DESC;
"""
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Plot the data
plt.figure(figsize=(8, 5))
sns.barplot(x='category', y='avg_dopamine_max', hue='category', data=df, palette='viridis', legend=False)
plt.title('Average Maximum Dopamine Increase by Category')
plt.xlabel('Category')
plt.ylabel('Average Maximum Dopamine Increase (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('dopamine_by_category.png')
print("Plot saved as 'dopamine_by_category.png'")