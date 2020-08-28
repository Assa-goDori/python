'''
Created on 2020. 8. 20.

@author: GDJ24
graph1.py : 그래프그리기
'''
#pip install ggplot
import matplotlib.pyplot as plt
plt.style.use("ggplot")
subjects=["Java","JSP","SPRING","HADOOP","PYTHON"]
print(range(len(subjects)))
subjects_index = range(len(subjects))
print(type(subjects))
scores = [65,90,85,60,95]   #수치데이터

fig = plt.figure()              #그래프를 그릴 공간. 도화지
ax1 = fig.add_subplot(1,1,1)    #도화지 분리. 1개의 도화지에 여러개의 그림이 가능
                                #현재 프로그램은 1개의 그림만 그림.
                                #1행1열 분리. => 그림 한개
                                #1 => 1번째 그림
#bar : 막대 그래프 설정
ax1.bar(subjects_index,scores,align="center",color="darkblue")
#axis,yaxis : 축설정
ax1.xaxis.set_ticks_position("bottom")
ax1.yaxis.set_ticks_position("left")

plt.xticks(subjects_index, subjects, rotation=0, fontsize="small")
plt.xlabel("Subject")   #x축 내용
plt.ylabel("Score")     #y축 내용
plt.title("Class Score")
#그래프를 img 파일로 저장
plt.savefig("bar_plot.png", dpi=400, bbox_inches="tight")
plt.show()