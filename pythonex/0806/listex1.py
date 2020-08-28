'''
Created on 2020. 8. 6.

@author: GDJ24
listex1.py : 리스트 예제(배열)
    파이썬 collection
    - 리스트(list) => []
    - 딕셔너리(dictionary, 자바에서의 Map) => {key, value}
    - 셋(set, 집합체) => {value}
    - 튜플(tuple, 상수처리된 리스트. 변경불가) => ()
'''
a = [0,0,0,0]
b = []
print(a,len(a))
print(b,len(b))

suma,sumb=0,0
for i in range(0,len(a)) :
    a[i] = int(input(str(i+1) + "번째 값 : ")) #str() : 문자열로 변경
    suma += a[i]
    b.append(a[i]) # b 리스트에 값을 추가. 자바함수:add()
    sumb += b[i]
print(a,len(a))
print(b,len(b))
print("a 리스트 합계 : ", suma)
print("b 리스트 합계 : ", sumb)
print(a[::-1])