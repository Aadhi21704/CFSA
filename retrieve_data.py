import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('customer_feedback.db')

# Fetch all feedback entries
query = "SELECT * FROM Feedback"
data = pd.read_sql_query(query, conn)

# Display the retrieved data
print(data.columns)

# Close the connection
conn.close()
