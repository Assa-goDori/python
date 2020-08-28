'''
Created on 2020. 8. 7.

@author: GDJ24
functionex1.py : 함수 사용하기
'''
# 함수 선언

def coffee_machine(button):
    print()
    print("#1 뜨거운 물 준비")
    print("#2 종이컵 준비")
    if button == 1 :
        print("#3 보통커피를 탄다.")
    elif button == 2 :
        print("#3 설탕커피를 탄다.")
    elif button == 3 :
        print("#3 블랙커피를 탄다.")
    print("#4 물을탄다.")
#함수의 끝
# main 부분
coffee = int(input("커피 종류를 입력하세요(1:보통, 2:설탕, 3:블랙)"))
coffee_machine(coffee)