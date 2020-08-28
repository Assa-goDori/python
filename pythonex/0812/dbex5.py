'''
Created on 2020. 8. 12.

@author: GDJ24
dbex5.py : mariadb에 데이터 추가하기
'''
import pymysql
conn = pymysql.connect(host="localhost",port=3306,
                       user="scott",passwd="1234",
                       db="classdb",charset="utf8")
cur = conn.cursor()
data = [
    (10, "바나나", 3000, "바나나는 길다."),
    (11, "망고", 5000, "망고는 열대 과일이다."),
    (12, "배", 2500, "배는 우리나라배가 제일 맛있다."),
    ]
d1,d2,d3,d4=data[0]
print(d1,d2,d3,d4)
for i in data :
    cur.execute('''insert into item (item_no, item_name, item_price, item_content)
            values(%s,%s,%s,%s)''',i);
cur.execute("select * from item")
for row in cur.fetchall() :
    print(row)
conn.rollback()