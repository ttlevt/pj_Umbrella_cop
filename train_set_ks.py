import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('./train/pusan_ttl.csv')

df2 = df.set_index(df['date'], drop=True, append=False)

df3 = df2.drop('date', axis=1)
li = []
cl = [] # 0: 맑음 0~1 1: 조금흐림 1~4 흐림 5이상       2번조건 0~1 : 맑음  이외=흐림
# 결과값 차이 거의 없으므로 그냥 2번조건 선택
for i in df3['hr']:
    if i == 0:
        li.append(i)
    else:
        li.append(1)
df3['hr'] = li
for i in df3['cloudy']:
    if i <= 1:
        cl.append(0)
    # elif i < 1 and i < 5:
    #     cl.append(1)
    else:
        cl.append(1)
df3['cloudy'] = cl
# print(df3)
# 강우시간이 0이 아니면(-값은 없으므로) 1로 변환 -> 1 = 우산필요, 0 = 우산필요X
# 전운량 3단계로 구분처리 하기 전(구분처리이유 크롤링해올 데이터에서는 전운량의 수치보다
# 맑음, 구름조금 , 흐림 단계로 가져올 것이기 때문에 학습시킬 알고리즘도 전운량의 단계화가
# 필요해 보임 -> 그냥 2단계로 진행 0 맑음 1 흐림으로
# --
x = df3[['cloudy', 'mm', 'percent']]
y = df3['hr']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=77)

from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier()
# print(x_train)
tree.fit(x_train, y_train)

predict = tree.predict(x_test)

from sklearn.metrics import classification_report
# print(predict)
tree.score
import pickle
pickle.dump(tree, open("weather_ks.pkl", "wb"))



# print(classification_report(y_test, predict))
# --
# df_merge = pd.DataFrame({'test':y_test , 'predict':predict})
# print(df_merge)

# print(tree.score(x_test,y_test))
# 다른 분석모델중 예측률이 높은 모델들과 별 차이없어서 그냥 결정나무 사용
'''
result = dict()
from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(x_train, y_train)
result['nb'] = nb.score(x_test, y_test)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
result['knn'] = knn.score(x_test, y_test)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(x_train, y_train)
result['lr'] = lr.score(x_test, y_test)

from sklearn.svm import SVC
svc = SVC()
svc.fit(x_train, y_train)
result['svc'] = svc.score(x_test, y_test)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=0)
rf.fit(x_train, y_train)
result['rf'] = rf.score(x_test, y_test)

from sklearn.ensemble import GradientBoostingClassifier
gbc = GradientBoostingClassifier(random_state=0)
gbc.fit(x_train, y_train)
result['gbc'] = gbc.score(x_test, y_test)

from xgboost import XGBClassifier
xgb = XGBClassifier(random_state=0)
xgb.fit(x_train, y_train)
result['xgb'] = xgb.score(x_test, y_test)

se1 = pd.Series(result).sort_values()
print(se1)
'''
# se1.plot(kind='barh')


