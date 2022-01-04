import pandas as pd
import numpy as np

total = pd.read_csv ('./data/19년도평가.csv',encoding='EUC-KR', index_col='학과') # 제일 첫번째로 오게 만듬
total.head()
total.info()
total.columns
#Index(['연도', '학과', '학생구분', '응시자수', 'A과목', 'B과목', 'F과목', 'D과목', 'G과목', 'C과목', 'E과목'], dtype='object')


total['A과목이수']
#Name: A과목이수, Length: 3478, dtype: int64
