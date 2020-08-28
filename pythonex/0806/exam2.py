'''
Created on 2020. 8. 5.

@author: GDJ24
exam2.py : 초를 입력받아 몇시간 몇분 몇초인지 출력하기
'''
time = int(input('초를 입력하세요'))
print(time,"초는 ", time//3600, "시간", end="")
time -= time//3600*3600
print(time//60, "분", end="")
print(time%60,"초 입니다.")