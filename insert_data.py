import sqlite3

# Sample data
feedback_data = [
    ("John Doe", "Great service but room for improvement.", "2024-11-12 10:00:00"),
    ("Jane Smith", "Not satisfied with the support team.", "2024-11-11 14:30:00"),
    ("Alice Brown", "Quick response and excellent support!", "2024-11-10 09:15:00"),
    ("Bob White", "The website was down for hours.", "2024-11-09 16:45:00")
]

# Connect to database
conn = sqlite3.connect("customer_feedback.db")
cursor = conn.cursor()

# Insert sample data
cursor.executemany('''
    INSERT INTO Feedback (CustomerName, FeedbackText, Timestamp)
    VALUES (?, ?, ?)
''', feedback_data)

print("Sample data inserted successfully!")

# Commit and close connection
conn.commit()
conn.close()
