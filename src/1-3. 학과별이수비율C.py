import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 7
matplotlib.rcParams['axes.unicode_minus'] = False #한글폰트 -깨짐현상

df = pd.read_csv('./data/1. 19년도-과정이수및평가점수.csv', usecols=[1,6])
# df.head()

all = df.groupby(['학과']).count()
# all.head()

comp = df[df['C과목이수'] == 1]
compc = comp.groupby(['학과']).count()
# compc.head()

rate=compc/all
rater=rate.round(2)
# rater.head()

ratedesc=rater.sort_values('C과목이수',ascending=False)
# ratedesc.head()
crate = ratedesc.reset_index()
crate.head()

plt.title('C과목이수율')
plt.xlabel('학과')
plt.ylabel('C과목이수')
plt.bar(crate['학과'],crate['C과목이수'],label='x축:학과 y축:이수율')
plt.legend()
plt.ylim([0,.4])
plt.xticks(rotation=45, ha='right')
plt.show()
