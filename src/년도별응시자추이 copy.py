import pandas as pd
import numpy as np

df = pd.read_csv('./data/numofdep.csv')
df.head()
df.groupby(['연도']).size

