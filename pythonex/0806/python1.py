'''
Created on 2020. 8. 5.

@author: GDJ24
python1.py : 파이썬 예제1

    1. ''' ''' 여러줄 주석
    2. # 한줄 주석
    3. 변수 선언 필요 없음(자료형 필요X, 처음으로 들어오는 값으로 자료형 자동선언, 자동형변환이 됨)
    4. { } 블럭이 없음. 공백으로 처리함.
'''
#한줄주석
print("Hello world!")

sel = int(input('입력 진수 결정(16/10/8/2) : '))
num = input("값 입력 : ")
if sel == 16 :
    num10 = int(num, 16)    #int() : 형변환 연산자, 문자열 num을 16진수로 인식하여 정수형 리턴
    print("%s 의 16진수  : %d" % (num, num10))
if sel == 10 :
    num10 = int(num, 10)
    print(num,"의 10진수 : ",num10)
if sel == 8 :
    num10 = int(num, 8)
    print(num,"의 8진수 : ",num10)
if sel == 2 :
    num10 = int(num, 2)
    print(num,"의 2진수 : ",num10)
print(num10)
print(type(num))
print(type(num10))

#10진수를 16, 8 ,2 진수로 변경하여 출력하기
print("16진수 =>",(hex(num10)))
print("8진수 =>",(oct(num10)))
print("2진수 =>",(bin(num10)))