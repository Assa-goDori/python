'''
Created on 2020. 8. 10.

@author: GDJ24
lambdaex2.py : 람다식을 이용한 리스트 처리
'''
myList=[1,2,3,4,5]

def add10(num):
    return num+10

for i in range(len(myList)) :
    myList[i] = add10(myList[i])
print(myList)

add = lambda num:num+10
for i in range(len(myList)) :
#    myList[i] = add(myList[i])
    myList[i] = (lambda num:num+10)(myList[i])  #함수객체를 직접 입력하여 사용가능
print(myList)