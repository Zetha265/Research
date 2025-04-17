import sqlite3

# Connect to a database file (or create it if it doesn't exist)
conn = sqlite3.connect('energy_data.db')

# Create a cursor to execute SQL commands
c = conn.cursor()

# Create the table to store energy measurements
c.execute('''
    CREATE TABLE IF NOT EXISTS energy_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        energy_wh INTEGER
    )
''')

# Save changes and close the connection
conn.commit()
conn.close()

print("Database and table created.")
