def select_pkl(place_name, data_rst):
    import pandas as pd
    lc = pd.read_csv('./apis/sector.csv', encoding='CP949')
    import pickle
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
    return result
# select_pkl('서울')