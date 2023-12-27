import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('example.db')

# Read CSV file into a DataFrame
df = pd.read_csv('example.csv')

# Write DataFrame to SQLite table
df.to_sql('my_table', conn, index=False, if_exists='replace')

# Commit and close
conn.commit()
conn.close()