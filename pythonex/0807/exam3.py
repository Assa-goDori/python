'''
Created on 2020. 8. 7.

@author: GDJ24
exam3.py : 간단한 계산기 함수
'''
def calc(v1, v2, op):
    result = 0
    if op == '+' :
        result = v1 + v2
    elif op == '-' :
        result = v1 - v2
    elif op == '*' :
        result = v1 * v2
    elif op == '/' :
        result = v1 / v2
    return result

oper = input("연산자를 선택하세요:(+,-,*,/) =>")
var1 = int(input("첫번째 수=>"))
var2 = int(input("두번째 수=>"))
res = calc(var1,var2,open)
print("계산 : %d %s %d = %d" % (var1,oper,var2,res))