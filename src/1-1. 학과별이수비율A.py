import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 7
matplotlib.rcParams['axes.unicode_minus'] = False #한글폰트 -깨짐현상


# 1.데이터 불러오기
df = pd.read_csv('./data/1. 19년도-과정이수및평가점수.csv', usecols=[1,4])
# df.head()
# df.info()

# 2. 비율 계산을 위한 학과 전체학생 및 이수 학생 수, 이수 비율 계산

# 2-1 학과별 전체 학생 수
all = df.groupby(['학과']).count()
# all.head()

# 2-2 학과별 이수한 학생 수
comp = df[df['A과목이수'] == 1]
compc = comp.groupby(['학과']).count()
# compc.head()

# 2-3 학과별 이수한 학생의 비율 계산 및 반올림
rate=compc/all
rater=rate.round(2)
# rater=rate['A과목응시']*100
# rater.head()

ratedesc=rater.sort_values('A과목이수',ascending=False)
# ratedesc.head()
crate = ratedesc.reset_index()
crate.head()

# 3.데이터 시각화
plt.title('A과목이수율')
plt.xlabel('학과')
plt.ylabel('A과목이수')
plt.bar(crate['학과'],crate['A과목이수'],label='x축:학과 y축:이수율')
plt.legend()
plt.ylim([0,.25])
plt.xticks(rotation=45, ha='right')
plt.show()

# compc = compc.reset_index()

# 차트 종류, 제목, 차트 크기, 범례, 폰트 크기 설정
# ax = ratedesc.plot(kind='bar', title='이수율', figsize=(12, 4), legend=True, fontsize=12)
# ax.set_xlabel('학과', fontsize=12)          # x축 정보 표시
# ax.set_ylabel('A과목이수', fontsize=12)     # y축 정보 표시
# ax.legend(['A과목이수'], fontsize=12)    # 범례 지정

