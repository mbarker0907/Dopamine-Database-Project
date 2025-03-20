import sqlite3
import pandas as pd
import plotly.express as px

# Connect to the database
conn = sqlite3.connect('dopamine.db')

# Query to calculate dopamine load by user, date, and category
query = """
SELECT au.user_id, au.date, a.category, 
       SUM(a.dopamine_max * (au.duration_minutes / 60.0)) AS dopamine_load
FROM Activity_Usage au
JOIN Activities a ON au.activity_id = a.activity_id
GROUP BY au.user_id, au.date, a.category;
"""
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Create an interactive grouped bar chart
fig = px.bar(
    df,
    x='user_id',
    y='dopamine_load',
    color='category',
    barmode='group',
    text='dopamine_load',
    title='Cumulative Dopamine Load by User and Category (2025-03-20)',
    labels={'user_id': 'User', 'dopamine_load': 'Dopamine Load (%)'},
    hover_data=['category', 'dopamine_load'],
)

# Customize the layout for a "cool" look
fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent paper background
    font=dict(family="Arial", size=14, color="#ffffff"),  # White font for contrast
    title_font=dict(size=20, color="#ffffff"),
    xaxis_title="User",
    yaxis_title="Dopamine Load (%)",
    xaxis=dict(showgrid=True, gridcolor="#444444", linecolor="#ffffff"),
    yaxis=dict(showgrid=True, gridcolor="#444444", linecolor="#ffffff"),
    legend_title="Category",
    legend=dict(font=dict(color="#ffffff")),
    margin=dict(l=50, r=50, t=80, b=50),
    template="plotly_dark"  # Dark theme for a sleek look
)

# Round the text labels on the bars and position them
fig.update_traces(
    texttemplate='%{text:.1f}',
    textposition='auto',
    marker=dict(line=dict(color='#000000', width=1))  # Black outline for bars
)

# Save the plot as an interactive HTML file
fig.write_html("dopamine_load_interactive.html")
print("Interactive plot saved as 'dopamine_load_interactive.html'")