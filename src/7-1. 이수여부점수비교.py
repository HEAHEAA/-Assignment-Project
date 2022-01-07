import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 7
matplotlib.rcParams['axes.unicode_minus'] = False #한글폰트 -깨짐현상

# 0.데이터 불러오기
dfA = pd.read_csv('./data/1. 19년도-과정이수및평가점수.csv', usecols=[4,9])
dfA.head()
dfA.info()

dfB = pd.read_csv('./data/1. 19년도-과정이수및평가점수.csv', usecols=[5,10])
dfB.head()
dfB.info()

dfC = pd.read_csv('./data/1. 19년도-과정이수및평가점수.csv', usecols=[6,11])
dfC.head()
dfC.info()

dfD = pd.read_csv('./data/1. 19년도-과정이수및평가점수.csv', usecols=[7,12])
dfD.head()
dfD.info()

dfE = pd.read_csv('./data/1. 19년도-과정이수및평가점수.csv', usecols=[8,13])
dfE.head()
dfE.info()


# 1. 이수자의 평균 점수 구하기
Ac_df = dfA[dfA['A과목이수'] == 1]
Acm_df = Ac_df.mean()
Acm_df

Bc_df = dfB[dfB['B과목이수'] == 1]
Bcm_df = Bc_df.mean()
Bcm_df

Cc_df = dfC[dfC['C과목이수'] == 1]
Ccm_df = Cc_df.mean()
Ccm_df

Dc_df = dfD[dfD['D과목이수'] == 1]
Dcm_df = Dc_df.mean()
Dcm_df

Ec_df = dfE[dfE['E과목이수'] == 1]
Ecm_df = Ec_df.mean()
Ecm_df


# 2. 미이수자의 평균 점수 구하기
Ai_df = dfA[dfA['A과목이수'] == 2]
Aim_df = Ai_df.mean()
Aim_df.head()

Bi_df = dfB[dfB['B과목이수'] == 2]
Bim_df = Bi_df.mean()
Bim_df

Ci_df = dfC[dfC['C과목이수'] == 2]
Cim_df = Ci_df.mean()
Cim_df

Di_df = dfD[dfD['D과목이수'] == 2]
Dim_df = Di_df.mean()
Dim_df

Ei_df = dfE[dfE['E과목이수'] == 2]
Eim_df = Ei_df.mean()
Eim_df

#하나의 데이터프레임으로 합쳐주기

all = pd.DataFrame({'과목':['A과목','B과목','C과목','D과목','E과목'],
    '이수자':[Acm_df['A과목점수'],Bcm_df['B과목점수'],Ccm_df['C과목점수'],Dcm_df['D과목점수'],Ecm_df['E과목점수']],
    '미이수자':[Aim_df['A과목점수'],Bim_df['B과목점수'],Cim_df['C과목점수'],Dim_df['D과목점수'],Eim_df['E과목점수']]})
# all.index = ['A과목','B과목','C과목','D과목','E과목']
all.head()

com = all.round(4)
com.head()

# 다른 버전
# Aim_df['A과목점수']
# all = pd.DataFrame({
#     'A':['A과목',Acm_df['A과목점수'],Aim_df['A과목점수']],
#     'B':['B과목',Bcm_df['B과목점수'],Bim_df['B과목점수']],
#     'C':['C과목',Ccm_df['C과목점수'],Cim_df['C과목점수']],
#     'D':['D과목',Dcm_df['D과목점수'],Dim_df['D과목점수']],
#     'E':['E과목',Ecm_df['E과목점수'],Eim_df['E과목점수']]
#     },index=['과목','이수자','미이수자'])

# all.head()
# # all = all.reset_index()
# com = all.round(4)
# com.head()



# # 3.데이터 시각화
plt.title('과목별 이수여부 점수비교') #그래프 이름 지어주기
plt.xlabel('과목') #y축 레이블 이름 지어주기
plt.ylabel('이수여부') #y축 레이블 이름 지어주기
plt.plot(com['과목'],com['이수자'],label='이수자 평균 점수',color='red') #x축, y축, 레이블 설명
plt.plot(com['과목'],com['미이수자'],label='미이수자 평균점수',color='blue') #x축, y축, 레이블 설명
plt.legend()
plt.ylim([3,5]) #y축 범위 설정
# plt.xticks(rotation=45, ha='right') #x축 항목 기울기 설정
plt.show()