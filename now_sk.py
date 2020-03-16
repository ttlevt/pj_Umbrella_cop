import requests
from bs4 import BeautifulSoup
import pandas as pd
from select_pkl import select_pkl

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
    skey = '&appKey=l7xxbca72c23f2a144839a2c531cfdde3ec3'
    url_ = baseurl+xy+skey
    # print(url_)
    response = requests.get(url_)
    assert response.status_code is 200
    dom = BeautifulSoup(response.content, "html.parser")

    zs = str(dom)


    mm = zs.split(',')[14][-5:-1]
    # print('mm:',mm)
    percent = zs.split(',')[10][-6:-1]

    sky = zs.split(',')[6][-4:-2]
    skytr = ''
    if sky == '맑음':
        skytr = 0
    else:
        skytr = 1
    print(url_)
    print('percent:', percent)
    print('sky:', skytr)
    now_li = [skytr, mm, percent]
    print(now_li)
    # result = select_pkl(place_name, apis_today)


now_sk('광주시')





