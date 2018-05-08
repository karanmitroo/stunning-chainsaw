import pandas as pd

#To remove BLANK values with their mean values
def clean_file(file_name):
    data = pd.read_csv(file_name, na_values = "?", header=None)
    # data.dropna()
    # for each in data.columns:
        # name = each
        # print data[each].mean()
        # data[each] = data[each].fillna(data[each].mean())
        
        
    # data.F = data.F.fillna(data.F.mean())
    data = data.fillna(data.mean())

    new_file_name = file_name.split('.')[0] + '_cleaned.csv'
    data.to_csv(new_file_name, header=False, index=False)

#To clean
def clean_data(data):
    data = pd.Series(data)
    data = data.fillna(data.mean())
    return data
