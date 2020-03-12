import requests
from bs4 import BeautifulSoup
# def getplace(place_name) :

# dict 이름만 원하는걸로 바꿔주면 되니까 천천히 하자 금방할수있음
def getplace(place_name):

    if len(place_name) > 4:
        place_name = place_name[0:2]
    if place_name[-1] == '시':
        place_name = place_name[0:-1]

    response = requests.get("https://www.weatheri.co.kr/forecast/forecast01.php?rid=0202040103&k=1&a_name=%EA%B0%80%ED%8F%89")

    assert response.status_code is 200
    dom = BeautifulSoup(response.content, "html.parser", from_encoding='utf-8')

    a_tag = dom.select('a')
    a_tag2 = (a_tag[88:260])
    name = []
    for i in a_tag2:
        name.append(i.text)
    # tag2 = a태그의 88~260까지 즉 모든지역들의 이름이 적힌 링크들을 name리스트에 담음
    print(name)
    li = []
    for i in a_tag2:
        tdx = str(i).split('?')[1]
        # 링크들을 하나씩 가져와서 ?뒤의 변동값들을
        tdx2 = str(tdx).split('"')[0]
        # 앞뒤로 잘라서 변동값만 추려낸 값을 li리스트에 담는다
        li.append(tdx2)
    loc = {name:value for name, value in zip(name, li)}
    # name리스트의 값(즉 지역명)과 li리스트(지역별링크)를 loc사전으로 묶는다
    if place_name in loc:
        # 입력받은 지역명이 사전에 있을경우 사전의 벨류값을 고정링크 후면에 이어붙여서 
        # 입력받은 지역명의 링크로 크롤링할 url을 지정한다

        response = requests.get("https://www.weatheri.co.kr/forecast/forecast01.php?"+str(loc.pop(place_name)) + '')
        assert response.status_code is 200
        dom = BeautifulSoup(response.content, "html.parser", from_encoding='utf-8')
    td = dom.select('td')
    # 해당페이지의 td를 선택자로 전부가져온다
    td_pic = td[334:340]
    # 운량을 이미지로 설정되있는걸 확인 후 이미지는 태그와 이미지파일명을 가져올것이고
    td_rain = td[352:358]
    # 강수량은 태그와 값을 가져올것임
    td_hum = td[370:376]
    # 습도역시 태그와 값을 가져옴
    #전운량 332~340
    
    # text값과 이미지태그값들을 가져왔으니 변환해서 새로운 리스트에 담아준다
    pic_li = []
    rain_li = []
    hum_li = []

    for pic in td_pic: # 전운량변환
        if str(pic)[-25] == '1' and str(pic)[-26] == '0' :
            #전운량 값을 인덱스 -26,-25번 순으로 비교했을때 두자리값이 01로 끝나면
            # 맑음이라는 0번을 저장
            pic_li.append(0)
        else :
            #아닐경우 흐림이라는 1번을 각각 리스트에 저장한다
            pic_li.append(1)

    for rain in td_rain: # 강수량변환
        if rain.text.strip() == '':
            # text가 없는경우 0번이라고 저장한다 = 결측치처리
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
    return(pic_li,rain_li,hum_li)

getplace('울산광역시')



