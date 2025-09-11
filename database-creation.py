import sqlite3 

conn = sqlite3.connect('scotsirishsaints.db')
cursor = conn.cursor()
print("connected")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Saints (
    SaintID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Sex TEXT,
    Birth_Date INTEGER,
    Death_Date INTEGER,
    Birth_Location TEXT,
    Death_Location TEXT,
    Death_Type TEXT
)        
''')