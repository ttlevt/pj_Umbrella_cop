from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd


def apis_Getplace(place_name):
    if place_name in ['부산','대구','인천','대전','광주','울산']:
        place_name = place_name+'광역시'
    # print(place_name)
    df = pd.read_csv('./apis/xy_data.csv', encoding='CP949')
    xy_li = []

    for i in df['x']:
        xy_li.append(i)
        #검색어 생각해보기
    locli = ['서울', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시',
             '울산광역시', '세종', '강화군', '백령도', '수원시', '성남시', '의정부시', '안양시',
             '부천시', '광명시', '평택시', '동두천시', '안산시', '고양시', '과천시', '구리시', '남양주시',
             '오산시', '시흥시', '군포시', '의왕시', '하남시', '용인시', '파주시', '이천시', '안성시', '김포시',
             '화성시', '광주시', '양주시', '포천시', '여주시', '연천군', '가평군', '양평군', '대관령',
             '춘천시', '원주시', '강릉시', '동해시', '태백시', '속초시', '삼척시', '홍천군', '횡성군',
             '영월군', '평창군', '정선군', '철원군', '화천군', '양구군', '인제군', '고성군', '양양군',
             '추풍령', '청주시', '충주시', '제천시', '보은군', '옥천군', '영동군', '증평군', '진천군',#69
             '괴산군', '음성군', '단양군', '천안시', '공주시', '보령시', '아산시', '서산시', '논산시',
             '계룡시', '당진시', '금산군', '부여군', '서천군', '청양군', '홍성군', '예산군', '태안군',
             '전주시', '군산시', '익산시', '정읍시', '남원시', '김제시', '완주군', '진안군', '무주군',
             '장수군', '임실군', '순창군', '고창군', '부안군', '흑산도', '목포시', '여수시', '순천시',
             '나주시', '광양시', '담양군', '곡성군', '구례군', '고흥군', '보성군', '화순군', '장흥군',
             '강진군', '해남군', '영암군', '무안군', '함평군', '영광군', '장성군', '완도군', '진도군',
             '신안군', '달성군', '포항시', '경주시', '김천시', '안동시', '구미시', '영주시', '영천시',
             '상주시', '문경시', '경산시', '군위군', '의성군', '청송군', '영양군', '영덕군', '청도군',#72
             '고령군', '성주군', '칠곡군', '예천군', '봉화군', '울진군', '울릉군', '독도', '창원시',
             '진주시', '통영시', '사천시', '김해시', '밀양시', '거제시', '양산시', '의령군', '함안군',
             '창녕군', '고성군', '남해군', '하동군', '산청군', '함양군', '거창군', '합천군', '고산군',#31
             '성산포', '성판악', '제주시', '서귀포시']
    loc_dict = dict()
    loc_dict = {name:value for name, value in zip(locli, xy_li)}
    # loc_dict으로 지역명과 좌표값을 사전형태로 묶어줌


    # place_name = '울산광역시'
    if place_name in loc_dict.keys():
        xy = loc_dict.pop(place_name)
    today = (str(datetime.today()).split()[0])
    today = int(today.replace('-', ''))-1

    baseurl = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst?'
    serv = 'serviceKey=oHgZfD9oeFM8cre%2BCD7dYf19ZdDFQMXdgk1wHMs8jmBvzvNvnimHQUQuAlWVD3dS1l78I1mHil41Z7ooft13mQ%3D%3D&'\
           'pageNo=1&numOfRows=80&dataType=XML&base_date={}&base_time=2330&{}'.format(today, xy)


    response = requests.get(baseurl+serv)

    # print(baseurl+serv)
    assert response.status_code is 200
    dom = BeautifulSoup(response.content, "html.parser")
    # sel2 = dom.select('items')
    fcstV = dom.select('fcstValue')
    vali = []
    for value in fcstV:
        vali.append(value.text)
    # print(baseurl+serv)
    # print(vali)
    cloudy = [vali[24],vali[35],vali[44],vali[56],vali[65],vali[76]]
    cli = []
    for i in cloudy:
        if i == '1':
            cli.append(0)
        else :
            cli.append(1)
    rain = [vali[32],vali[53],vali[73]]
    rain2 = []
    reh = [vali[23],vali[33],vali[43],vali[54],vali[64],vali[74]]
    # 강수량이 6시간마다누적되므로 실제값은 4개뿐이라서 8개로 늘리도록함-> 패치 6개로 줄임
    for i in rain:
        rain2.append(int(i)/2)
        rain2.append(int(i)/2)

    # print(baseurl+serv)
    # print('cloudy:', cli, 'rain:', rain2, 'reh:', reh)


    tli= [cli]+[rain2]+[reh]

    idx = [9,12,15,18,21,0]

    col = ['cloudy', 'mm', 'percent']
    #
    # apis_today = pd.DataFrame.from_records(tli, columns=col, index=idx,)
    # print(apis_today)
    # apis_today = pd.DataFrame.from_records(tli)
    # ex = pd.DataFrame(data=cli, index=idx ,columns=['cloudy'])
    apis_today = pd.DataFrame(data=cli, index=idx, columns=['cloudy'])
    apis_today['mm'] = rain2
    apis_today['percent'] = reh


    # print(apis_today)
    # print(place_name)
    import pickle
    from sklearn import tree
    tree = pickle.load(open("weather.pkl", "rb"))
    result = tree.predict(apis_today)
    if 1.0 in result:
        a = 1  # 1 필요  0 불필요
    else:
        a = 0
    return a

# a= apis_Getplace('광주시')
# print(a)

#클라우드  mm percent









# 전운량 시작 4번째 15 25 36 45 57 66 77
# 강수량  12 33 54 74
# 습도 시작 3 13 24 34 44 55 65 75
# b = apis_Getplace('울산')
# print(b)

#     base_time=2300 # base_time은 작일 2300 or 2330 부터 조회해야 3시데이터부터쭉나온다
