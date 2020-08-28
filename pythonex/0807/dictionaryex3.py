'''
Created on 2020. 8. 7.

@author: GDJ24
dictionaryex3.py : 
'''

import operator
dic,list = {}, []
dic = {"Thomas":"토마스","Edward":"에드워드","Henry":"헨리","Gothem":"고든","James":"제임스"}
list = sorted(dic.items(), key=operator.itemgetter(0), reverse=True)
#sorted : 정렬하기
#dic.items() : 내부의 튜플 객체
#operator.itemgetter(0) : 정렬기준을 튜플 객체의 첫번째(key)로 설정(영문)
#reverse=True 내림차순 정렬
print(type(list))
print(list)
#operator.itemgetter(1) : 정렬기주늘 튜플 객체의 두번째(value)로 설정(한글)
#reverse 생략시 자동 오름차순 정렬
list = sorted(dic.items(), key=operator.itemgetter(1))
print(list)