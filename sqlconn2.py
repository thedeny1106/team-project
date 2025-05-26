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
print('데이터 개수 ', len(rows))
for row in rows: print(row['EMPNO'], row['ename'], row['SAL'])

sql = '''
insert into emp(empno, ename, sal) values(%s, %s, %s)
'''


# cursor.execute(sql, (9000, '백승빈', 6000))
conn.commit()

sql = 'select ifnull(max(empno), 0) + 1 from emp'
cursor.execute(sql)
rows = cursor.fetchone()
for row in rows: print(row)

conn.close()