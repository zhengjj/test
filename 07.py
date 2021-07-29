import sqlite3

conn = sqlite3.connect('test.db')
c =conn.cursor()
c.execute('''INSERT INTO STUDENT(ID,NAME,AGE,ADDDRESS) VALUES (1,'测试',18,'福建厦门')''')
c.execute('''INSERT INTO STUDENT(ID,NAME,AGE,ADDDRESS) VALUES (2,'测试2',9,'福建福州')''')
conn.commit()
conn.close