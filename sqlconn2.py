import pymysql
import pymysql.cursors

conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'user02',
    passwd = 'qwer1234',
    db = 'mydb'
)

cursor = conn.cursor(pymysql.cursors.DictCursor)
ename = 'SCOTT'
sql = "select * from emp where ename = '" + ename + "'"
print(sql) 
cursor.execute(sql)
rows = cursor.fetchall()
print(len(rows))