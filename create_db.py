# Create a database
import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE movie_review(review TEXT , sentiment TEXT)')
print ("Table created successfully")
conn.close()