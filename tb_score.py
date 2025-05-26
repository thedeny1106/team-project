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

#insert
def insert():
    sname = input('이름 : ')
    kor = int(input('국어 : '))
    eng = int(input('영어 : '))
    math = int(input('수학 : '))

    sql = 'insert into tb_score(sname, kor, eng, math, regdate) values(%s, %s, %s, %s, now())'

    cursor.execute(sql, (sname, kor, eng, math))
    conn.commit()
#select
def select():
    sql = 'select * from tb_score'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows: print(row)

#update
def update():
    target  = int(input('수정 학생 학생번호 : '))
    sname = input('이름 : ')
    kor = int(input('국어 : '))
    eng = int(input('영어 : '))
    math = int(input('수학 : '))
    sql = 'update tb_score set sname = %s, kor = %s, eng = %s, math = %s where id = %s'
    cursor.execute(sql, (sname, kor, eng, math, target))
    conn.commit()

#delete
def delete():
    target  = int(input('삭제 학생 학생번호 : '))
    sql = 'delete from tb_score where id = %s'
    cursor.execute(sql, (target))
    conn.commit()

insert(); select(); update(); select(); delete(); select()
