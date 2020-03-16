#-*- coding: utf-8 -*-

from apisdata_craw import apis_Getplace
from weatheri_today import wei_getplace
from apisdata_tom import apis_Getplace_tom
from weatheri_tom import wei_getplace_tom


def cross_v(place_name):
    val1 = apis_Getplace(place_name)
    val2 = wei_getplace(place_name)
    rst_today = ''
    rst_tom = ''
    if val1 == val2:
        if val1 == 0:
            rst_today ='sunny'
        else :
            rst_today ='rainy'
    val3 = apis_Getplace_tom(place_name)
    val4 = wei_getplace_tom
    if val3 == val4:
        if val3 == 0:
            rst_tom = 'sunny'
        else:
            rst_tom = 'rainy'
    return('today:' + rst_today + ' tomorrow:' + rst_tom)

# a = cross_v('울산광역시')
# print(a)