'''
Created on 2020. 8. 5.

@author: GDJ24
exam1.py : 금액을 입력받아 동전으로 바꿔주는 프로그램 작성하기
    동전의 종류 : 500, 100, 50, 10, 5, 1
    입력받은 금액을 동전으로 바꿔 줄 때 동전의 갯수는 최소개로 한다.  
'''
count = int(input('금액을 입력하세요'))
count500 = count//500
print("500원 : ", count500)
count -= count500*500
count100 = count//100
print("100원 : ", count100)
count -= count100*100
count50 = count//50
print("50원 : ", count50)
count -= count50*50
count10 = count//10
print("10원 : ", count10)
count -= count10*10
count5 = count//5
print("5원 : ", count5)
count -= count5*5
count1 = count//1
print("1원 : ", count1)