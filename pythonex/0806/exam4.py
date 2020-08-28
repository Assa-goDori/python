'''
Created on 2020. 8. 6.

@author: GDJ24
exam4.py : 삼각형 출력하기

삼각형이 높이를 입력 받은 후 삼각형을 출력하는 프로그램을 작성하기
'''
num = int(input('삼각형의 높이를 입력하세요'))
for i in range(1, num+1) :
    print("*"*i)
print()
for i in range(num, 0, -1) :
    print("*"*i)
print()
for i in range(1, num+1) :
    print(" "*(num-i),end="")
    print("*"*i)
print()
for i in range(num, 0, -1) :
    print(" "*(num-i),end="")
    print("*"*i)
for i in range(num, 0, -1) :
    print(" "*(num-i),"*"*i)
    
print()
for i in range(1, num+1) :
    print(" "*(num-i),end="")
    print("*"*(2*i-1))

print()
for i in range(num, 0, -1) :
    print(" "*(num-i),end="")
    print("*"*(2*i-1))