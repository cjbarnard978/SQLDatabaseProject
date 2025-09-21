

import sqlite3 
conn = sqlite3.connect('scotsirishsaints.db')
cursor = conn.cursor()
print('connected')


cursor.execute('''
CREATE TABLE IF NOT EXISTS Attributes (
    M_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Miracle_Type TEXT
)
''')
print ('created')
conn.commit()
print('closed')