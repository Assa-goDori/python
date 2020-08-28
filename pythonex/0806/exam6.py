'''
Created on 2020. 8. 6.

@author: GDJ24
exam6.py : 리스트 문제.
    aa, bb 배열을 생성하고, aa 배열은 0부터 짝수 20개를 저장, bb 배열은 aa 배열의 역순으로 값을 저장
    aa, bb 배열의 값을 출력하기
'''
even = 0
i = 0
aa = []
while True :
    aa.append(even)
    i += 1
    even += 2
    if (len(aa)==20) :
        break

bb = []
i = 0
while True :
    if (i == 20) :
        break;
    bb.append(aa[::-1][i])
    i+=1
print(aa)
print(bb)