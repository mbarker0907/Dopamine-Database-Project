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

# Create the Activity_Usage table with a foreign key to Activities
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Activity_Usage (
        usage_id INTEGER PRIMARY KEY AUTOINCREMENT,
        activity_id INTEGER NOT NULL,
        user_id TEXT NOT NULL,
        date TEXT NOT NULL,
        duration_minutes INTEGER NOT NULL,
        FOREIGN KEY (activity_id) REFERENCES Activities(activity_id)
    )
''')

# Insert sample data into Activities (if not already present)
activities_data = [
    ('Methamphetamine', 1200, 1200, 'Substance', 'Highest spike, extremely addictive'),
    ('Cocaine', 225, 225, 'Substance', 'Significant spike, addictive'),
    ('Social Media (e.g., Instagram, TikTok)', 75, 100, 'Digital', 'Random rewards, potentially addictive'),
    ('Video Games', 75, 100, 'Digital', 'Reward-based, potentially addictive'),
    ('Movies/TV Shows (Watching)', 40, 60, 'Digital', 'Emotional reward, varies by content'),
    ('Exercise (e.g., Running, Yoga)', 50, 75, 'Natural', 'Natural boost, healthy reward'),
    ('Meditation (e.g., Mindfulness, Zazen)', 25, 50, 'Mindful', 'Calming, low-intensity reward')
]
cursor.executemany('INSERT OR IGNORE INTO Activities (activity_name, dopamine_min, dopamine_max, category, notes) VALUES (?, ?, ?, ?, ?)', activities_data)

# Insert sample data into Activity_Usage
usage_data = [
    (3, 'UserA', '2025-03-20', 120),  # Social Media for 2 hours
    (6, 'UserA', '2025-03-20', 30),   # Exercise for 30 minutes
    (7, 'UserA', '2025-03-20', 15),   # Meditation for 15 minutes
    (3, 'UserB', '2025-03-20', 60),   # Social Media for 1 hour
    (4, 'UserB', '2025-03-20', 90)    # Video Games for 1.5 hours
]
cursor.executemany('INSERT OR IGNORE INTO Activity_Usage (activity_id, user_id, date, duration_minutes) VALUES (?, ?, ?, ?)', usage_data)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database created and data inserted successfully!")