
import pandas as pd
plname='b'
li = [['a', 'b', 'c', 'd'],['e','f','g','h'],['i','j','k','l']]
column = ['kk', 'kaw', 'jeju', 'ks']
df = pd.DataFrame(li, columns=column)
# print(df)
# print(plname)
# print(type(df['kaw']))
kli = []
kli = df['kaw']
print(kli)
print(type(kli))
if plname in df['kaw'].values:
    print("있음")
else:
    print('없음')
# 이로써 df의 값만 검색하는거 확인
