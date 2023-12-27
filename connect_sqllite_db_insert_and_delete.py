import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES ('John', 30)")

# Delete data
cursor.execute("DELETE FROM users WHERE name = 'John'")

# Commit and close
conn.commit()
conn.close()