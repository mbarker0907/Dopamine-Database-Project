import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('dopamine.db')
cursor = conn.cursor()

# Create the Activities table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Activities (
        activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
        activity_name TEXT NOT NULL,
        dopamine_min INTEGER NOT NULL,
        dopamine_max INTEGER NOT NULL,
        category TEXT,
        notes TEXT
    )
''')

# Insert data
activities_data = [
    ('Methamphetamine', 1200, 1200, 'Substance', 'Highest spike, extremely addictive'),
    ('Cocaine', 225, 225, 'Substance', 'Significant spike, addictive'),
    ('Social Media (e.g., Instagram, TikTok)', 75, 100, 'Digital', 'Random rewards, potentially addictive'),
    ('Video Games', 75, 100, 'Digital', 'Reward-based, potentially addictive'),
    ('Movies/TV Shows (Watching)', 40, 60, 'Digital', 'Emotional reward, varies by content'),
    ('Exercise (e.g., Running, Yoga)', 50, 75, 'Natural', 'Natural boost, healthy reward'),
    ('Meditation (e.g., Mindfulness, Zazen)', 25, 50, 'Mindful', 'Calming, low-intensity reward')
]
cursor.executemany('INSERT INTO Activities (activity_name, dopamine_min, dopamine_max, category, notes) VALUES (?, ?, ?, ?, ?)', activities_data)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database created and data inserted successfully!")