import sqlite3
conn = sqlite3.connect('scotsirishsaints.db')
cursor = conn.cursor()
print("connected")

cursor.execute('''
DELETE FROM Saints;
''')
print('done')
conn.commit()
