from textblob import TextBlob
import sqlite3
import pandas as pd

# Function to classify sentiment
def classify_sentiment(feedback):
    analysis = TextBlob(feedback)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Connect to SQLite database
conn = sqlite3.connect('customer_feedback.db')

# Fetch all feedback entries
query = "SELECT * FROM Feedback"
data = pd.read_sql_query(query, conn)

# Apply sentiment analysis to each feedback
data['Sentiment'] = data['FeedbackText'].apply(classify_sentiment)

# Display results
print(data[['CustomerName', 'FeedbackText', 'Sentiment']])

# Close the connection
conn.close()
