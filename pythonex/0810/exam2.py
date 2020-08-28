'''
Created on 2020. 8. 10.

@author: GDJ24
exam2.py : 문자열 문제
'''

ss="홍길동"
# 홍#길#동# 로 출력하기
for i in range(len(ss)) :
    print(ss[i], end="#")
print()
# 동길홍 로 출력하기
print(ss[::-1])