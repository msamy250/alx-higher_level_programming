#!/usr/bin/python3
import MySQLdb


db = MySQLdb.connect(
    host="localhost",
    user="yourusername",
    passwd="yourpassword",
    db="testdb"
)


cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print(f"MySQL version: {data}")

db.close()
