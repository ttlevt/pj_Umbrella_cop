# 내일의 날씨 크롤링해서 가져오기
import requests
from bs4 import BeautifulSoup
import pandas as pd


def wei_getplace_tom(place_name):

    if len(place_name) > 4:
        place_name = place_name[0:2]
    if place_name[-1] == '시':
        place_name = place_name[0:-1]
    response = requests.get(
        "https://www.weatheri.co.kr/forecast/forecast01.php?rid=0202040103&k=1&a_name=%EA%B0%80%ED%8F%89")
    # print(("https://www.weatheri.co.kr/forecast/forecast01.php?&k=1&a_name="+str(place_name)+""))
    assert response.status_code is 200
    dom = BeautifulSoup(response.content, "html.parser", from_encoding='utf-8')

    a_tag = dom.select('a')
    a_tag2 = (a_tag[88:260])
    name = []
    for i in a_tag2:
        name.append(i.text)
    # tag2 = a태그의 88~260까지 즉 모든지역들의 이름이 적힌 링크들을 name리스트에 담음

    li = []
    for i in a_tag2:
        tdx = str(i).split('?')[1]
        # 링크들을 하나씩 가져와서 ?뒤의 변동값들을
        tdx2 = str(tdx).split('"')[0]
        # 앞뒤로 잘라서 변동값만 추려낸 값을 li리스트에 담는다
        li.append(tdx2)
    loc = {name: value for name, value in zip(name, li)}
    # name리스트의 값(즉 지역명)과 li리스트(지역별링크)를 loc사전으로 묶는다
    if place_name in loc:
        # 입력받은 지역명이 사전에 있을경우 사전의 벨류값을 고정링크 후면에 이어붙여서
        # 입력받은 지역명의 링크로 크롤링할 url을 지정한다
        response = requests.get("https://www.weatheri.co.kr/forecast/forecast01.php?" + str(loc.pop(place_name)) + '')
        assert response.status_code is 200
        dom = BeautifulSoup(response.content, "html.parser", from_encoding='utf-8')

    td = dom.select('td')
    # 해당페이지의 td를 선택자로 전부가져온다

    # 내일 운량 393~401
    td_pic = td[395:401]
    td_rain = td[413:419]
    # 강수량은 태그와 값을 가져올것임
    td_hum = td[431:437]
    # text값과 이미지태그값들을 가져왔으니 변환해서 새로운 리스트에 담아준다
    pic_li2 = []
    rain_li2 = []
    hum_li2 = []

    for pic in td_pic:  # 전운량변환
        if str(pic)[-25] == '1' and str(pic)[-26] == '0':
            # 전운량 값을 인덱스 -26,-25번 순으로 비교했을때 두자리값이 01로 끝나면
            # 맑음이라는 0번을 저장
            pic_li2.append(0)
        else:
            # 아닐경우 흐림이라는 1번을 각각 리스트에 저장한다
            pic_li2.append(1)

    for rain in td_rain:  # 강수량변환
        if rain.text.strip() == '':
            # text가 없는경우 0번이라고 저장한다 = 결측치처리
            rain_li2.append(0)
        else:
            rain_li2.append(rain.text.strip())

    for h in td_hum:  # 습도변환
        if h.text.strip() == '':
            hum_li2.append(0)
        else:
            hum_li2.append(h.text.strip())
    idx = [9, 12, 15, 18, 21, 0]
    wei_tom = pd.DataFrame(data=pic_li2, index=idx, columns=['cloudy'])
    wei_tom['mm'] = rain_li2
    wei_tom['percent'] = hum_li2

    import pickle
    tree = pickle.load(open("weather.pkl", "rb"))
    pre_result = tree.predict(wei_tom)

    # umli = []
    # for i in pre_result:
    #     if i > 0:
    #         umli.append('1')
    #     else :
    #         umli.append('0')
    # um = ""
    a = 0

    if 1.0 in pre_result:
        a = 1  # 1 필요  0 불필요
    else:
        a = 0
    return a




b=wei_getplace_tom('울릉도')
print(b)
