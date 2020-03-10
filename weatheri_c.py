import requests
from bs4 import BeautifulSoup
# def getplace(place_name) :
def getplace(place_name):
    response = requests.get("https://www.weatheri.co.kr/forecast/forecast01.php?rid=0202040103&k=1&a_name=%EA%B0%80%ED%8F%89")
    # print(("https://www.weatheri.co.kr/forecast/forecast01.php?&k=1&a_name="+str(place_name)+""))
    assert response.status_code is 200
    dom = BeautifulSoup(response.content, "html.parser", from_encoding='utf-8')

    a_tag = dom.select('a')
    a_tag2 = (a_tag[88:260])
    name = []
    for i in a_tag2:
        name.append(i.text)
    li = []
    for i in a_tag2:
        tdx = str(i).split('?')[1]
        tdx2 = str(tdx).split('"')[0]
        li.append(tdx2)
    loc = {name:value for name, value in zip(name, li)}

    if place_name in loc:
        response = requests.get("https://www.weatheri.co.kr/forecast/forecast01.php?"+str(loc.pop(place_name)) + '')
        assert response.status_code is 200
        dom = BeautifulSoup(response.content, "html.parser", from_encoding='utf-8')
    td = dom.select('td')
    td_pic = td[332:340]
    td_rain = td[350:358]
    td_hum = td[368:376]
    #전운량 332~340
    pic_li = []
    rain_li = []
    hum_li = []

    for pic in td_pic: # 전운량변환
        if str(pic)[-25] == '1' and str(pic)[-26] == '0' :
            pic_li.append(0)
        else :
            pic_li.append(1)

    for rain in td_rain: # 강수량변환
        if rain.text.strip() == '':
            rain_li.append(0)
        else :
            rain_li.append(rain.text.strip())

    for h in td_hum: # 습도변환
        if h.text.strip() == '':
            hum_li.append(0)
        else :
            hum_li.append(h.text.strip())

    print('전운량:', pic_li)  # 0 = 맑음 1= 구름있음
    print('강수량 :', rain_li) # 0 = 강수량없음
    print('습도 :', hum_li)


getplace('구례')




