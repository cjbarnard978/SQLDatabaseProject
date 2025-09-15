import sqlite3
conn = sqlite3.connect('scotsirishsaints.db')
cursor = conn.cursor()
print("connected")

cursor.execute('''
INSERT INTO sources (sourceID, Title, Author, Year, Language)
VALUES ('Ancient Lives of Scottish Saints', 'Translator W.M. Metcalfe', '1895', 'English'),
       ('Chronicle of the Scottish Nation', 'John of Fordun Translator Felix Skene', '1872', English),
       ('Martyrology of Oengus the Culdee', 'Whitley Stokes', '1905', 'English'),
       ('Martyrology of Donegal', 'Father Michael OClery Translator Todd and Reeves', '1864', 'English),
       ('Annals of Ireland of the Four Masters,'Translator Owen Connellan, Esq.', '1846', 'English'),
       ('Vitae Sanctorum Hiberniae', 'Charles Plummer', '1910', 'Latin');     
''')

conn.close()
print('data entered')