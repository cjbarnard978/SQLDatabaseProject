import sqlite3 
conn = sqlite3.connect('scotsirishsaints.db')
cursor = conn.cursor()
print('connected')