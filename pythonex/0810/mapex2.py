'''
Created on 2020. 8. 10.

@author: GDJ24
mapex2.py : 람다를 이용하여 map 처리 하기
'''

mylist = [1,2,3,4,5]
#map을 이용하여 mylist 각각의 값에 10 더하기
add = lambda num:num+10
mylist = list(map(add,mylist))
print(mylist)

#
mylist = [1,2,3,4,5]
mul = lambda num:num*10
mylist = list(map(mul,mylist))
print(mylist)   #[10,20,30,40,50]로 출력

list1 = [1,2,3,4]
list2 = [10,20,30,40]
hap = lambda n1,n2,n3:n1+n2+n3
haplist = list(map(hap,list1,list2,mylist))
print(haplist)