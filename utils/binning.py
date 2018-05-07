import random


def binning(k, categorical):
    """
    A list of dictionaries for each attribute that tells which 
    value to be mapped with which new value.
    """
    mapping = []

    #Adding dictionaries to the list
    for i in range(len(categorical[0])):
        mapping.append({})

    """
    Mapping all the values randomly to new values in range 1 - k both inclusive. 
    Also checking if already mapped then considering the same value.
    """
    for each_tuple in categorical:
        for i in range(len(each_tuple)):
            try:
                each_tuple[i] = mapping[i][each_tuple[i]]
            except:
                mapping[i][each_tuple[i]] = random.randint(1,k)
                each_tuple[i] = mapping[i][each_tuple[i]]

    # for each_dict in mapping:
    
    #     for i in range(1,k+1):
    #         try:
    #             print i, (each_dict.values()).count(i)
    #         except:
    #             pass

    return categorical
