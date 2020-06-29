#coding:gbk
#python3不再支持MySQLdb,以下项目来自网络
import pymysql

#获取版本
db = pymysql.connect('localhost','','','TEST')
cursor =  db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Version:',data)
#建表
cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')
sql1 = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql1)
#插入
sql2 = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, "M", 2000)"""
try:
    cursor.execute(sql2)
    db.commit()
except:
    db.rollback()
#查询
sql3 = "SELECT * FROM EMPLOYEE WHERE INCOME > %s" % (1000)
cursor.execute(sql3)
res = cursor.fetchall()
for row in res:
    fname = row[0]
    iname = row[1]
    page = row[2]
    psex = row[3]
    income = row[4]
    print(fname,iname,page,psex,income)
#更新
sql4 = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   cursor.execute(sql4)
   db.commit()
except:
   db.rollback()

#删除
sql5 = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()