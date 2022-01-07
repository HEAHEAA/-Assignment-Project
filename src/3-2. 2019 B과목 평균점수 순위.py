import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 7
matplotlib.rcParams['axes.unicode_minus'] = False #한글폰트 -깨짐현상

df = pd.read_csv('./-Assignment-Project/data/2. 15-19년전체집계.csv', usecols=[0,1,2,5])
df.head()

year2019 = df['연도'] == 2019
year2019
students2019 = df[year2019]
students2019
#-----------------------------------------------
new2019 = students2019['학생구분'] == '신입생'
fm2019 = students2019[new2019]
fm2019
#---------------------------------------------
old2019 = students2019['학생구분'] == '재학생'
sn2019 = students2019[old2019]
sn2019


fmdesc=fm2019.sort_values('B과목',ascending=False)
fmdesc

#------------------------------------------------------
sndesc = sn2019.sort_values('B과목',ascending=False)
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
plt.title('2019학과별B과목점수')
plt.xlabel('학과')
plt.ylabel('B과목점수')
plt.legend()
plt.ylim([2.0,6.0])
plt.show()

#-----------------------------------------------------------------------


