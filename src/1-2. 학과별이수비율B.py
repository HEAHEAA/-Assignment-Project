import pandas as pd
import numpy as np

df = pd.read_csv('./data/1. 19년도-과정이수및평가점수.csv', usecols=[1,5])
# df.head()

all = df.groupby(['학과']).count()
# all.head()

comp = df[df['B과목이수'] == 1]
compc = comp.groupby(['학과']).count()
# compc.head()

rate=compc/all
rater=rate.round(2)
# rater.head()

ratedesc=rater.sort_values('B과목이수',ascending=False)
ratedesc.head(5)
