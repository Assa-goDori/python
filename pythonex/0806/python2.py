'''
Created on 2020. 8. 5.

@author: GDJ24
python2.py : input(), print() 함수
    input("입력전 출발 문자열") : 입력받은 값은 문자열 형태로 입력받는다.
    print(출력값1, 출력값2, ...) : 여러개 출력시 ,로 연결 가능하다.
'''
a = int(input("값1 입력 : "))
b = int(input("값2 입력 : "))
result = a + b
print(a, "+", b, "=", result)
print(a, "+", b, "=", a+b)
#print(a+"+"+b+"="+result) #오류 발생, 문자열과 정수형은 +로 묶을 수 없다.
print("%d + %d = %d" % (a,b,result))
print("{0:d} + {1:d} = {2:d}".format(a,b,result))
print("안녕하세요 ", end="") #end에 기본적으로 "\n"이 설정 되어있어서 자동 ln이 됨(end값을 초기화 시켜주면 붙여쓰기 가능)
print("홍길동 입니다.")

print("""동해물과 백두산이
    마르고 닳도록
    하느님이 보우하사
    우리 나라 만세  
    """)

print('''동해물과 백두산이
    마르고 닳도록
    하느님이 보우하사
    우리 나라 만세  
    ''')
#print에서 주석 사용시 입력값 그대로 출력