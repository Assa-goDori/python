'''
Created on 2020. 8. 11.

@author: GDJ24
classex4.py : 클래스에서 사용되는 메서드
'''

class Line :
    length = 0
    def __init__(self,length) :
        self.length = length
    # 자바에서의 toString() 메서드 기능
    def __repr__(self):
        return "선의 길이 : " + str(self.length)
    def __add__(self,other):        #같은 객체간에 연산자 사용시 호출되는 메서드 => 연산자 오버로딩
        print("더하기 연산자 호출")
        return self.length + other.length
    def __lt__(self,other):         # lt, gt 둘중에 하나만 구현하면 처리 가능
        print("< 연산자 호출")
        return self.length < other.length
    def __gt__(self,other):
        print("> 연산자 호출")
        return self.length > other.length
    def __eq__(self,other):
        print("== 연산자 호출")
        return self.length == other.length
    def __del__(self):              #소멸자 : 객체가 소멸될 때 호출되는 메서드(소멸자는 오버로딩 불가함)
        print(self.length, "길이의 선이 제거 되었습니다.")

myline1 = Line(200) # __init__ 호출. 생성자 호출. 객체 생성시 호출되는 메서드
myline2 = Line(100)
print(myline1)      # __repr__ 호출. toString 메서드와 같은 기능
print(myline2)

print("두 선의 길이의 합: ",myline1+myline2)   # __add__ 호출.
#두 선의 길이 비교하기
if myline1.length < myline2.length :
    print("myline2 선이 더 깁니다.")
elif myline1.length == myline2.length :
    print("두 선의 길이가 같습니다.")
else :
    print("myline1 선이 더 깁니다.")
    
if myline1 < myline2 :              # __lt__ 호출, False
    print("myline2 선이 더 깁니다.")
elif myline1 == myline2 :           # __eq__ 호출, False
    print("두 선의 길이가 같습니다.")
elif myline1 > myline2 :            # __gt__ 호출, True
    print("myline1 선이 더 깁니다.")
#프로그램 종료. => 객체 소멸. __del__ 호출. 소멸자 호출.