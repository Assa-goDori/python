'''
Created on 2020. 8. 6.

@author: GDJ24
listex2.py : 리스트의 기본함수
'''
mylist = [30,10,20]
print("리스트 : %s" % mylist)
mylist.append(40)
print("mylist.append(40) 후 리스트 : %s" % mylist)
#pop() : 마지막 요소 제거 리턴. 스택의 명령어
print("pop() 메서드 결과 : %s" % mylist.pop())
print("mylist.pop() 후 리스트 : %s" % mylist)
mylist.sort()
print("mylist.sort() 후 리스트 : %s" % mylist)
mylist.reverse()
print("mylist.reverse() 후 리스트 : %s" % mylist)

print("20값 위치 : %d" % mylist.index(20))
mylist.insert(2, 15)
print("mylist.insert(2, 15) 후 리스트 : %s" % mylist)
mylist.remove(15)
print("mylist.remove(15) 후 리스트 : %s" % mylist)

# extend : 다른 리스트를 덧붙이기 vs append : 요소 한개를 덧붙이기
mylist.extend([77,77,99])
print("mylist.extend([77,77,99]) 후 리스트 : %s" % mylist)
print("77 값의 갯수 : %d" % mylist.count(77))

# 리스트에서 find 함수 사용 불가
#print("77 값의 갯수 : %d" % mylist.find(77))