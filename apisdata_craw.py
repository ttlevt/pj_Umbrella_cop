from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

df = pd.read_csv('./apis/apisget.csv', encoding='cp949')
print(df)

# http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst?
# &&&&&&

# def apis_Getplace(place_name):
#
#     today = (str(datetime.today()).split()[0])
#     today = today.replace('-', '')
#     print(today)
#     serviceKey = 'oHgZfD9oeFM8cre%2BCD7dYf19ZdDFQMXdgk1wHMs8jmBvzvNvnimHQUQuAlWVD3dS1l78I1mHil41Z7ooft13mQ%3D%3D'
#     pageNo=1
#     numOfRows=80 확정값 말고
#     dataType=XML
#     base_date=today
#     base_time=0500
#     nx=60 입력값대체
#     ny=120 입력값 대체