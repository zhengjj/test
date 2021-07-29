import pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='',db='test',charset='utf8')
c =conn.cursor()

c.execute('''select count() from home''')
conn.commit()

print(c.fetchall())

conn.close()