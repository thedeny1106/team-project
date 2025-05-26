#pip install pymysql
import pymysql

conn = pymysql.connect(
    host = 'localhost', 
    port = 3306,
    user = 'user02', passwd = 'qwer1234',
    db = 'mydb'
    )

cursor = conn.cursor()
print('접속 성공')

sql = 'select * from emp'
cursor.execute(sql) # sql 실행 결과를 cursor객체에 저장

rows = cursor.fetchall() # tuple형식 -> 테이블 튜플, 행 튜플
for row in rows: print(type(row), row)

print('하나만 가져오기')
sql = 'select * from emp where empno = 8005'
cursor.execute(sql)
row = cursor.fetchone()
print(row)


print('세개만 가져오기')
sql = 'select * from emp where empno in (8001, 8002, 8003)'
cursor.execute(sql)
rows = cursor.fetchmany(3)
for row in rows: print(row)

cursor = conn.cursor(pymysql.cursors.DictCursor)
cursor.execute(sql)
rows = cursor.fetchmany(3)
for row in rows: print(row)

conn.close()

