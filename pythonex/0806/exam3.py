'''
Created on 2020. 8. 5.

@author: GDJ24
exma3.py : 숫자를 입력받아 입력된 값까지의 전체합, 짝수합, 홀수합 구하기
'''
num = int(input('숫자를 입력하세요'))

sum = 0
for i in range(0, num+1) :
    sum += i
print("0부터 ", num, "까지의 합 : ", sum)
sum = 0
for i in range(0, num+1, 2) :
    sum += i
print(num, "까지의 짝수 합 : ", sum)
sum = 0
for i in range(1, num+1, 2) :
    sum += i
print(num, "까지의 홀수 합 : ", sum)