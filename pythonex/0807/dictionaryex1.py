'''
Created on 2020. 8. 7.

@author: GDJ24
dictionaryex1.py : 딕셔너리 예제 
'''

singer = {}
singer['이름']='트와이스'
singer['구성원수']=9
singer['데뷔곡']='우아하게'
singer['소속사']='JYP'
singer['소속사']='SM'  #map에서 같은 key에 다른 value값을 넣으면 오류가 발생x value값이 수정
#singer.keys() : dictionary의 key의 값들만 리턴
for i in singer.keys() :
    print("%s => %s" % (i,singer[i]))
print(singer['이름'])#트와이스
print(singer)
print(type(singer))
print(type(singer.keys()))
print(str(list(singer.keys())) + "*****")   #키셋을 리스트 형태로 변경