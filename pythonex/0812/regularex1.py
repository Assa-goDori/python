'''
Created on 2020. 8. 12.

@author: GDJ24
regularex1.py : 정규식 예제. 정규식 사용 안함
'''

data = '''
    park 800805-1234567
    kim 800905-2345678
    choi 750905-a123456
'''

result = []
for line in data.split("\n") :
#line : park 800805-1234567
    word_result = []
    for word in line.split(" ") :
        #word[0] : park, work[1] : 800805-1234567
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit() :
            word = word[:6]+"-"+"*******"
        word_result.append(word)
        #work_result : [park,800805-*******]
    result.append(" ".join(word_result))
    #result : [park 800805-*******]
print("\n".join(result))