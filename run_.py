#-*- coding: utf-8 -*-

from apisdata_craw import apis_Getplace
from weatheri_today import wei_getplace
from apisdata_tom import apis_Getplace_tom
from weatheri_tom import wei_getplace_tom
from now_sk import now_sk
#cross_vali 
# 검증을 통해서 보다 더 정확한 값을 출력
def cross_v(place_name):
    # print(place_name)
    val0 = now_sk(place_name)
    val1 = apis_Getplace(place_name)
    val2 = wei_getplace(place_name)
    # print('val0:', val0, 'val1:', val1, 'val2:',val2)
    rst_today = ''
    rst_tom = ''
    # rst를 통한 오늘 내일 결과값 저장변수
    # print('v1+v2=', val1+val2)
    if val0 + val1 + val2 > 0:
        rst_today = "rainy"
    elif val1+val2 == 0 and val0 > 0:
        rst_today = "rainy"
    else:
        rst_today = "sunny"
    val3 = apis_Getplace_tom(place_name)
    val4 = wei_getplace_tom(place_name)
    # print('v3+v4:', val3+val4)
    if val3+val4 == 0:
        rst_tom = "sunny"
    else:
        rst_tom ="rainy"
    # print('rst_tom=', rst_tom)
    return('today:' + rst_today + ' tomorrow:'+ rst_tom)

# a = cross_v('울산')
# print(a)