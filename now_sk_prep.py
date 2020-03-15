import pandas as pd
# 검색 URL 적어놓고
#https://apis.openapi.sk.com/weather/current/hourly?lat=33&lon=126&appKey=l7xxbca72c23f2a144839a2c531cfdde3ec3
xy = pd.read_csv('./apis/dfs.csv', encoding='utf-8')
li1 = []
li2 = []
xyli = []
for i in xy['longi']:
    li1.append('lon='+str(i))
xy['longi'] = li1
for i in xy['lati'] :
    li2.append('&lat='+str(i))
xy['lati'] = li2
for i, j in zip(xy['longi'], xy['lati']):
    xyli.append(i+j)
xy['xy'] = xyli
xy2 = xy.drop(xy[['longi', 'lati']], axis=1)
print(xy2)
xy2.to_csv('./apis/xy_data2.csv', encoding='utf-8', index=False)






# 검색어받을시에 사전형태에서 좌표값 받아오는거

# 그 좌표값 이용해서 크롤링한 후

# 해당값 알고리즘으로 돌리는거까지



