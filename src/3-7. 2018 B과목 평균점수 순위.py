#3-7. 2018 B과목 평균점수 순위.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 7
matplotlib.rcParams['axes.unicode_minus'] = False #한글폰트 -깨짐현상

df = pd.read_csv('./-Assignment-Project/data/2. 15-19년전체집계.csv', usecols=[0,1,2,5])
df.head()

year2018 = df['연도'] == 2018
year2018
students2018 = df[year2018]
students2018
#-----------------------------------------------
new2018 = students2018['학생구분'] == '신입생'
fm2018 = students2018[new2018]
fm2018
#---------------------------------------------
old2018 = students2018['학생구분'] == '재학생'
sn2018 = students2018[old2018]
sn2018


fmdesc=fm2018.sort_values('B과목',ascending=False)
fmdesc

#------------------------------------------------------
sndesc = sn2018.sort_values('B과목',ascending=False)
sndesc

#------------------------------------------
deDic = {}
for i,dept in enumerate(df['학과'].unique()) :
    deDic[dept] = i
deDic

fmdList = [deDic[v] for v in fmdesc['학과']]
fmdList
sndList = [deDic[v]+0.4 for v in sndesc['학과']]
sndList
fmdesc['B과목']
plt.bar(fmdList,fmdesc['B과목'],label='신입생', color='r',width=0.5)
plt.bar(sndList,sndesc['B과목'],label='재학생', color='b',width=0.5)
plt.xticks(list(deDic.values()), labels=list(deDic.keys()), rotation=45, ha='right')

#신입생 학과 -> 숫자 0:기계, 1:화학

#재학생 학과 -> 0.3:기계, 위의 신입생 학과에 + 0.3
plt.title('2018학과별B과목점수')
plt.xlabel('학과')
plt.ylabel('B과목점수')
plt.legend()
plt.ylim([2.0,6.0])
plt.show()

#-----------------------------------------------------------------------


