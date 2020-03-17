import pandas as pd

def select_pkl(place_name, data_rst):
    from sklearn.tree import DecisionTreeClassifier
# lc = pd.read_csv('./apis/sector.csv', encoding='CP949')
    import pickle
# try:
# print(lc)
# 가정 시작
    tree = pickle.load(open("weather_kk.pkl", "rb"))
    result = tree.predict(data_rst)
    return result

# 가정 끝
'''    
if place_name in lc['kk'].values:
    from sklearn import tree
    tree = pickle.load(open("weather_kk.pkl", "rb"))
    result= tree.predict(data_rst)
elif place_name in lc['kw'].values:
    from sklearn import tree
    tree = pickle.load(open("weather_kw.pkl", "rb"))
    result= tree.predict(data_rst)
elif place_name in lc['cc'].values:
    from sklearn import tree
    tree = pickle.load(open("weather_cc.pkl", "rb"))
    result= tree.predict(data_rst)
elif place_name in lc['jl'].values:
    from sklearn import tree
    tree = pickle.load(open("weather_jl.pkl", "rb"))
    result= tree.predict(data_rst)
elif place_name in lc['ks'].values:
    from sklearn import tree
    tree = pickle.load(open("weather_ks.pkl", "rb"))
    result = tree.predict(data_rst)
else:
    from sklearn import tree
    tree = pickle.load(open("weather_jj.pkl", "rb"))
    result = tree.predict(data_rst)
# except Exception as e:
    # print(e)
return result
'''