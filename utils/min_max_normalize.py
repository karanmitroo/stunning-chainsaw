from sklearn.preprocessing import MinMaxScaler

def min_max_normalize(k, data):
    scaler = MinMaxScaler(feature_range=(1, k), copy=False)
    return scaler.fit_transform(data)