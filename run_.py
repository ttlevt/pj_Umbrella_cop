
from apisdata_craw import apis_Getplace
from weatheri_today import wei_getplace

def cross_v(place_name):
    val1 = apis_Getplace(place_name)
    val2 = wei_getplace(place_name)
    if val1 == val2:
        if val1 == 0:
            return('우산필요없음')
        else :
            return('우산필요함')
    else:
        return('아직잘모름')
        

# a = cross_v('울산광역시')
# print(a)