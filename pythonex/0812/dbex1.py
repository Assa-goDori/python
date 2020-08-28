'''
Created on 2020. 8. 12.

@author: GDJ24
dbex1.py : sqlite db 사용하기
'''

import sqlite3      #sqllite db 모듈
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)  #test.sqlite db에 접속
cur = conn.cursor() #cursor() : 명령 전달 객체
#여러 문장을 실행
cur.executescript('''
    drop table if exists items;
    create table items (item_id integer primary key,
        name text unique,
        price integer);
    insert into items (name, price) values ('Apple',800);
    insert into items (name, price) values ('Orange',500);
    insert into items (name, price) values ('Banana',300);
''')
conn.commit()   # Transaction 완료(commit : 정상처리 <-> rollback : 취소)
cur = conn.cursor()
cur.execute("select * from items")
item_list = cur.fetchall()
print(type(item_list))  #list형태
for it in item_list :
    print(it)