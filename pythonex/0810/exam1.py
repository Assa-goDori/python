'''
Created on 2020. 8. 10.

@author: GDJ24
exam1.py : 피보나치 수열 출력하기

피보나치 수열의 요소 갯수를 입력하세요(3이상의 값) : 10
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

'''
def fibo(a) :
    list=[0, 1]
    for i in range(0, a) :
        if (len(list)== a) :
            break
        list.append(list[i]+list[i+1])
    return list
    
num = int(input("피보나치 수열의 요소 갯수를 입력하세요(3이상의 값) : "))
print("f(",num,")=",end="")
print(fibo(num))