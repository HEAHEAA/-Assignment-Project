import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv('./data/1. 19년도-과정이수및평가점수.csv', usecols=[1,4])
# df.head()
df.info()

all = df.groupby(['학과']).count()
# all.head()

comp = df[df['A과목이수'] == 1]
compc = comp.groupby(['학과']).count()
# compc.head()

rate=compc/all
rater=rate.round(2)
# rater.head()

ratedesc=rater.sort_values('A과목이수',ascending=False)
ratedesc.head(5)
print(ratedesc.head(5))

# plt.plot(ratedesc)
# plt.show()

# plt.pie('A과목이수', labels='학과', autopct='%.2f%%')
# plt.show()

# dep = []
# ratio = ratedesc.readline()

# while data:
#     data=ratedesc.readline()
#     if not data:
#         break
#     dep.append(data.split(',')[2])

# depname=list(set(dep))
# cnt=[dep.count(i) for i in depname]

# print('depname:',depname)
# print('cnt:',cnt)

# plt.pie(cnt,labels=depname,autopct='%.1f%%')
# plt.show()





# data_f = open("data/Seoul_pop1.csv")

# # 년도 리스트
# years = []
# # 인구수 리스트
# populations = []

# for line in data_f: 
#     (year, population) = line.split(',')       
#     years.append(int(year))
#     populations.append(int(population))

# data_f.close() 


# # 학과 리스트
# deps = []
# # 비율 리스트
# orates = []

# for line in ratedesc: 
#     (학과, A과목이수) = line.split(',')       
#     deps.append(object(학과))
#     orates.append(int(A과목이수))

# ratedesc.close() 

# print(deps)