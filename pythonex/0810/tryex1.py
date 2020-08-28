'''
Created on 2020. 8. 10.

@author: GDJ24
tryex1.py : 예외 처리.
'''

mystr = "파이썬 공부 중입니다. 열심히 파이썬을 공부 합시다."
strpos = [] #파이썬 문자의 위치 정보 저장
index = 0
while True :
#    index = mystr.find("파이썬",index)
#    if index == -1 :
#        break
    try :
        index = mystr.index("파이썬",index)
        strpos.append(index)
        index +=1
    except :
        break
    
print("파이썬 문자의 위치 : ", strpos, ", 문자갯수:", len(strpos))