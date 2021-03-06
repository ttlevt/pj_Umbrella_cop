import pandas as pd
import numpy as np
import glob
import os

input_file = r'./project_data/suwon'
# 데이터를 전부 만들고 폴더정리를 했으므로 차후에 실행시 경로 확인하기
output_file = r'./project_data/suwon/suwon_ttl.csv'
# 합칠 파일들의 위치와 합쳐진후 저장할 파일의 이름 및 경로를 지정한다.
allFile_list = glob.glob(os.path.join(input_file, 'SURFACE*'))
# glob함수로 surface_로 시작하는 파일들을 모은다
print(allFile_list)
allData = []  # 읽어 들인 csv파일 내용을 저장할 빈 리스트를 하나 만든다
for file in allFile_list:
    df = pd.read_csv(file, encoding='cp949')
    allData.append(df)
dataCombine = pd.concat(allData, axis=0, ignore_index=True)
dataCombine.to_csv(output_file, index=False)


df = pd.read_csv('./project_data/suwon/suwon_ttl.csv', encoding='utf8')

df2 = df.drop(df.columns[[0,2,3,4,5,6,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,25,
                          26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,
                          46,47,48,49,50,51,52,53,54,55,56,57,58]], axis=1)
# 우리에게 필요한 컬럼은 강수지속시간, 강수량, 전운량, 습도 4개이므로 나머지삭제
output_file = r'./project_data/suwon/suwon_ttl.csv'
df2.to_csv(output_file, index=False)
