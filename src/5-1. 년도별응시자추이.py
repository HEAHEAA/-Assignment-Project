import pandas as pd
import numpy as np

df = pd.read_csv('./data/2. 15-19년전체집계.csv', usecols=[0,1,2,3])
df.head()
df.info
# 연도별 응시자 수
all = df.groupby(['연도']).sum('응시자수')
all.head()
<<<<<<< HEAD




=======
>>>>>>> 0cd517ed2ed6978344e723d3a41570753f358a8d
# 연도별 응시 학과 수-실패
second = df.groupby(['연도'and'학과'])
second.head()
df.groupby(['연도']).size
<<<<<<< HEAD

# second.groupby(['연도']).size










=======
>>>>>>> 0cd517ed2ed6978344e723d3a41570753f358a8d
q2=df.duplicated(['연도','학과'])
q2.head()
df[df.duplicated(['연도','학과'])==True]
df_drop = df.drop_duplicates(['연도','학과'])
df_drop
df_drop.to_csv('./data/numofdep.csv', index=False, encoding='UTF-8')
droppeddf = pd.read_csv('./data/numofdep.csv')
droppeddf.head()
droppeddf.groupby(['연도']).size
