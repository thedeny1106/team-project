#주급계산 아이디, 근무시간, 시간당급여, 연장수당
import pymysql
import pymysql.cursors

class WageInfo:
    def __init__(self, userid, workername, workhour, wage):
        self.userid = userid
        self.workername = workername
        self.workhour = workhour
        self.wage = wage

def calcPlus(workhour, wage):
    return max(wage // 2 * (workhour - 20), 0)


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
    userid = input('아이디 : ')
    username = input('이름 : ')
    workhour = int(input('근무시간 : '))
    wage = int(input('시간당급여 : '))
    plus = calcPlus(workhour, wage)

    sql = 'insert into work_info(worker_id, worker_name, work_hour, wage, extend_wage) values(%s, %s, %s, %s, %s)'

    cursor.execute(sql, (userid, username, workhour, wage, plus))
    conn.commit()

#select
def select():
    sql = 'select * from work_info'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows: print(row)

#update
def update():
    target  = int(input('수정 근로자 번호 : '))
    userid = input('아이디 : ')
    username = input('이름 : ')
    workhour = int(input('근무시간 : '))
    wage = int(input('시간당급여 : '))
    plus = calcPlus(workhour, wage)
    sql = 'update work_info set worker_id = %s, worker_name = %s, work_hour = %s, wage = %s, extend_wage = %s where id = %s'
    cursor.execute(sql, (userid, username, workhour, wage, plus, target))
    conn.commit()

#delete
def delete():
    target  = int(input('삭제 근로자 번호 : '))
    sql = 'delete from work_info where id = %s'
    cursor.execute(sql, (target))
    conn.commit()

insert(); select(); update(); select(); delete(); select(); cursor.close()