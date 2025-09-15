import sqlite3
conn = sqlite3.connect('scotsirishsaints.db')
cursor = conn.cursor()
print("connected")

cursor.execute('''
INSERT INTO sources (sourceID, Title, Author, Year, Language) VALUES
    (1, 'Ancient Lives of Scottish Saints', 'Translator W.M. Metcalfe', '1895', 'English'),
    (2, 'Chronicle of the Scottish Nation', 'John of Fordun Translator Felix Skene', '1872', 'English'),
    (3, 'Martyrology of Oengus the Culdee', 'Whitley Stokes', '1905', 'English'),
    (4, 'Martyrology of Donegal', 'Father Michael OClery Translator Todd and Reeves', '1864', 'English'),
    (5, 'Annals of Ireland and the Four Masters', 'Translator Owen Connellan Esq', '1846', 'English'),
    (6, 'Vitae Sanctorum Hiberniae', 'Charles Plummer', '1910', 'Latin');     
''')
print('data pushed')
conn.commit()
conn.close()
print('data entered')
