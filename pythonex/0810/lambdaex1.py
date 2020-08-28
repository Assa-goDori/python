'''
Created on 2020. 8. 10.

@author: GDJ24
lambdaex1.py : 람다식으로 함수 구현
'''
def hap(num1,num2):
    res = num1 + num2
    return res

print(hap(10, 20))  #30

#람다방식으로 구현
hap1 = lambda num1,num2:num1+num2   #lambda 매개변수 : 리턴값        java형식 : (num1, num2) => num1+num2
print(hap1(10,20))

#람다방식으로 곱셈의 결과 출력
mul1 = lambda num1,num2:num1*num2
print(mul1(10,20))

#매개변수 초기화 하기
hap2 = lambda num1=0,num2=1:num1+num2
print(hap2())
print(hap2(100))    # 첫번째 매개변수로 값이 설정됨(2번째 매개변수 X)
print(hap2(100,200))