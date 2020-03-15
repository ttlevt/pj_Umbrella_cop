import requests
from bs4 import BeautifulSoup
import pandas as pd


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
    response = requests.get(url_)
    assert response.status_code is 200
    dom = BeautifulSoup(response.content, "html.parser")
    cd = dom.find("pre")
    print(cd)
    # print(dom)
    # print(dom['SKY'].values())

now_sk('광주')





