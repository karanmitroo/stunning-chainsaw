import pandas as pd

file_name = 'processed_switzerland.csv'
data = pd.read_csv(file_name, na_values = "?")
# data.dropna()
# for each in data.columns:
    # name = each
    # print data[each].mean()
    # data[each] = data[each].fillna(data[each].mean())
    
    
# data.F = data.F.fillna(data.F.mean())
data = data.fillna(data.mean())

data.to_csv(file_name)
