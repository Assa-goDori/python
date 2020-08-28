'''
Created on 2020. 8. 6.

@author: GDJ24
exam5.py : 가로 구구단 출력하기
'''
i, j = 0,0
for i in range(2, 10) :
    print("%5d단 출력\t\t" % i, end="")
print()

for i in range(2, 10) :    
    for j in range(2, 10) :
        print("%2d X %2d = %3d\t\t" % (j,i,(i*j)), end="")
    print()