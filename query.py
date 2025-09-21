import sqlite3 
conn = sqlite3.connect('scotsirishsaints.db')
cursor = conn.cursor()
print('connected')

query1 = """
SELECT 
    Birth_Location, COUNT(*)
FROM Saints s
WHERE Birth_Location = 'Leinster, Ireland'
GROUP BY Sex;
"""
cursor.execute(query1)
results1 = cursor.fetchall()
print('results')
for row in results1:
    print(row)

query2 = """
SELECT
    Birth_Location, COUNT(*)
FROM Saints s
WHERE Birth_Location = 'Munster, Ireland'
GROUP BY Sex;
"""
cursor.execute(query2)
results2 = cursor.fetchall()
conn.close()
for row in results2:
    print(row)

conn.close()