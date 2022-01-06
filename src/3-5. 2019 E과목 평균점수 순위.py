import pandas as pd
import numpy as np

df = pd.read_csv('./data/2. 15-19년전체집계.csv', usecols=[0,1,8])
df.head()

is_2019 = df['연도'] == 2019
year2019 = df[is_2019]
year2019
year2019.info()

ratedesc=year2019.sort_values('E과목',ascending=False)
ratedesc