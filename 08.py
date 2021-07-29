import sqlite3

conn = sqlite3.connect('test.db')
c=conn.cursor()
c.execute('SELECT * FROM STUDENT')
conn.commit()
print(c.fetchall())
conn.close