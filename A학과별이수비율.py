import pandas as pd
import numpy as np

df = pd.read_csv('./data/1. 19년도-과정이수및평가점수.csv', usecols=[1,4])
# df.head()

all = df.groupby(['학과']).count()
# all.head()

comp = df[df['A과목이수'] == 1]
compc = comp.groupby(['학과']).count()
# compc.head()

rate=compc/all
# rate.head()

ratedesc=rate.sort_values('A과목이수',ascending=False)
ratedesc.head(5)