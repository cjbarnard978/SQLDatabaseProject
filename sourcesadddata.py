import sqlite3
conn = sqlite3.connect('scotsirishsaints.db')
cursor = conn.cursor()
print("connected")

cursor.execute('''
INSERT INTO TABLE sources (Title, Author, Year, Language)
VALUES ('Ancient Lives of Scottish Saints', 'Trans. W.M. Metcalfe', '1895', 'English'),
       ('Chronicle of the Scottish Nation', 'John of Fordun: Trans. Felix Skenes', '1872', English),
       ('Martyrology of Oengus the Culdee', 'Whitley Stokes', '1905', 'English'),
       ('Martyrology of Donegal', 'Fr. Michael O'Clery: Trans. Todd and Reeves', '1864', 'English),
       ()    
''')