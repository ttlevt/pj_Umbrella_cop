#-*- coding: utf-8 -*-

from apisdata_craw import apis_Getplace
from weatheri_today import wei_getplace

def cross_v(place_name):
    val1 = apis_Getplace(place_name)
    val2 = wei_getplace(place_name)
    if val1 == val2:
        if val1 == 0:
            return('sunny')
        else :
            return('rainy')
    else:
        return('not yet')
        

# a = cross_v('울산광역시')
# print(a)