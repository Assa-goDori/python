'''
Created on 2020. 8. 12.

@author: GDJ24
dbex4.py : mariadb 사용하기
'''
import pymysql  #pip install pymysql : cmd창에서 입력시 자동으로 설치시작

conn = pymysql.connect(host="localhost",port=3306,
                       user="scott",passwd="1234",
                       db="classdb",charset="utf8")
try :
    cur = conn.cursor() #명령전달객체
    cur.execute("select * from item")
#    for row in cur.fetchall() :    #모든 레코드 조회
#        print(row[0],row[1],row[2])
    while True :
        row = cur.fetchone()    #한개의 레코드만 조회
        if row == None :        #조회된 레코드가 없는 경우
            break
        print(row)
finally :
    cur.close()
    conn.close()