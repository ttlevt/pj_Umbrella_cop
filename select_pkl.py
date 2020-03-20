import pandas as pd

def select_pkl(place_name, data_rst):
    from sklearn.tree import DecisionTreeClassifier
    lc = pd.read_csv('./apis/sector.csv', encoding='CP949')
    # 지역분류파일 read
    import pickle
    # print(place_name)
# try:
# print(lc)
    # tree = pickle.load(open("weather_kk.pkl", "rb"))
    # result = tree.predict(data_rst)
    # return result
    if place_name in lc['kk'].values:
        # 요청명이 지역별 컬럼에 해당하는값이라면
        tree = pickle.load(open("weather_kk.pkl", "rb"))
        # 해당지역의 자료로 피클링했던 알고리즘을 언피클링해서 결과를 반환함
        # print('kk')
        result= tree.predict(data_rst)
    elif place_name in lc['kw'].values:
        tree = pickle.load(open("weather_kw.pkl", "rb"))
        # print('kw')
        result= tree.predict(data_rst)
    elif place_name in lc['cc'].values:
        tree = pickle.load(open("weather_cc.pkl", "rb"))
        # print('cc')
        result= tree.predict(data_rst)
    elif place_name in lc['jl'].values:
        # print('jl')
        tree = pickle.load(open("weather_jl.pkl", "rb"))
        result= tree.predict(data_rst)
    elif place_name in lc['ks'].values:
        # print('ks')
        tree = pickle.load(open("weather_ks.pkl", "rb"))
        result = tree.predict(data_rst)
    else:
        tree = pickle.load(open("weather_jj.pkl", "rb"))
        # print('jj')
        result = tree.predict(data_rst)
    # except Exception as e:
        # print(e)
    return result
# df = [0, 0, 70]
# df2 = pd.DataFrame([df])
# a = select_pkl('울릉군', df2)
# print(a)