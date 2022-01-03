import pandas as pd

total = pd.read_csv ('./data/1519전체집계.csv')
total.head()

#칼럼정보
total.columns 
#Index(['연도', '학과', '학생구분', '응시자수', 'A과목', 'B과목', 'F과목', 'D과목', 'G과목', 'C과목', 'E과목'], dtype='object')
#인덱스정보  RangeIndex(start=0, stop=278, step=1)
total.index 
total.to_numpy()
total.info()
