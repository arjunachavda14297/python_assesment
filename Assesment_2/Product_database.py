'''
import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',passwd='')
cur=db.cursor()
try:
    cur.execute(" create database Product ")
    db.commit()
    db.close()
    print('success')
except Exception as ex:
    print(ex)

'''
'''
import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',passwd='',database='product')
cur=db.cursor()
try:
    cur.execute(" create table product(pid bigint(10) primary key,pname varchar(50) not null,prise float(20) not null) ")
    db.commit()
    db.close()
    print('success')
except Exception as ex:
    print(ex)
'''

