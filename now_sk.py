import requests
from bs4 import BeautifulSoup
import pandas as pd
from select_pkl import select_pkl
import json

def now_sk(place_name):
    #이름값 조건문 적어놓기
    if place_name in ['부산', '대구', '인천', '대전', '광주', '울산']:
        place_name = place_name + '광역시'
    df = pd.read_csv('./apis/xy_data2.csv')
    kdict = dict()
    for i, j in zip(df['name'], df['xy']):
        kdict.setdefault(i, j)
    if place_name in kdict.keys():
        xy = kdict.pop(place_name)

    baseurl = 'https://apis.openapi.sk.com/weather/current/hourly?'
    # 기본 페이지 (필수파라미터 X)
    skey = '&appKey=l7xxbca72c23f2a144839a2c531cfdde3ec3'
    # 필수 파라미터값 
    url_ = baseurl+xy+skey
    # xy = 받아온 지역명의 경도 위도
    # print(url_)
    response = requests.get(url_)
    assert response.status_code is 200
    dom = BeautifulSoup(response.content, "html.parser")
    # bs4 cl
    zs = str(dom)
    # bs4타입은 json타입으로 변환이 바로 되지 않으므로 str타입으로 다시저장
    json_data = json.loads(zs)
    #import한 json모듈로 json타입으로 재변환 시킨 다음
    # print(json_data) 찍어보니 잘나오는거같다 하지만
    # print(json_data['weather']['hourly']['sky']['code'])
    # 원하는데이터에 한번에 접근을 못함.. 겁나 포장해놔서...
    jd2  = json_data['weather']['hourly'][0]
    # 필요한부분을 다시 도려내고
    # print(jd2['precipitation']['sinceOntime'])
    # 출력을하면 짜잔하고 원하는값이 나온단다 ㅠㅠ
    sky = jd2['sky']['name']
    #하늘상태 텍스트로 받아오면 숫자로 재가공
    if sky == '맑음':
        sky = 0
    else :
        sky = 1
    # 머신러닝 돌릴수 있도록 다시 하늘값 변경해주고

    percent = jd2['humidity']
    # 습도 역시 지정해주고
    mm = jd2['precipitation']['sinceOntime']
    # 강우량 ( 현재 날씨데이터이므로 현재강우량임 )


    # print(url_)
    now_li = [sky, mm, str(percent)]
    # print(now_li)

    now_li = pd.DataFrame([now_li], columns=['cloudy', 'mm', 'percent'])
    # print(now_li)
    result = select_pkl(place_name, now_li)
    return int(result)

# a = now_sk('대전')
# print(a)






