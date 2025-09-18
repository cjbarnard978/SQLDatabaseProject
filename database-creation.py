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
print ('created')

cursor.execute('''
CREATE TABLE IF NOT EXISTS sources (
    sourceID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT, 
    Author TEXT,
    Year INTEGER,
    Language TEXT
)
''')
print ('created')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Attributes (
    M_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Miracle_Type TEXT
)
''')
print ('created')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Events (
    Event_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    sourceID INTEGER, 
    saintID INTEGER, 
    M_ID INTEGER,
    FOREIGN KEY (sourceid) REFERENCES sources (sourceid),
    FOREIGN KEY (saintID) REFERENCES Saints (SaintID),
    FOREIGN KEY (M_ID) REFERENCES Attributes (M_ID)
)
''')
print("created")

conn.close()
print('DBs created')