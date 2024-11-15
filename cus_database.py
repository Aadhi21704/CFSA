import sqlite3

# Connecting to SQLite database 
conn = sqlite3.connect("customer_feedback.db")
cursor = conn.cursor()

# Create the Feedback table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Feedback (
        FeedbackID INTEGER PRIMARY KEY AUTOINCREMENT,
        CustomerName TEXT,
        FeedbackText TEXT,
        Timestamp DATETIME
    )
''')

print("Table 'Feedback' created successfully!")

# Commit and close the connection
conn.commit()
conn.close()
