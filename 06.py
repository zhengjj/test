import sqlite3

conn = sqlite3.connect('test.db')

c= conn.cursor()
c.execute('''CREATE TABLE STUDENT(
	    ID INT PRIMARY KEY  NOT NULL,
	    NAME  TEXT   NOT NULL,
	    AGE     INT NOT NULL,
	    ADDDRESS CHAR(50)
	    )''')
conn.commit()
conn.close()
