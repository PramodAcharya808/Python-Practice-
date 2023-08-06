import requests
import sqlite3

# Make API request
api_url = 'https://api.example.com/data'
response = requests.get(api_url)
data = response.json()

# Connect to SQLite database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Create table if not exists
create_table_query = '''
CREATE TABLE IF NOT EXISTS api_data (
    id INTEGER PRIMARY KEY,
    name TEXT,
    value INTEGER
);
'''
cursor.execute(create_table_query)
conn.commit()

# Insert data into the database
for item in data:
    name = item['name']
    value = item['value']

    insert_query = '''
    INSERT INTO api_data (name, value) VALUES (?, ?);
    '''
    cursor.execute(insert_query, (name, value))
    conn.commit()

# Close the database connection
conn.close()










































