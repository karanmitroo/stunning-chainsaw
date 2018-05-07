# from numerical.numerical import numerical_dist
import numpy
import random


# print numerical_dist(1, 43)

data = numpy.loadtxt("datasets/tae.csv", delimiter=",", usecols = (0,1,2,3))

categorical = data[:, (1,2)]
k = 3

mapping = []
for i in range(len(categorical[0])):
    mapping.append({})

for each_tuple in categorical:
    for i in range(len(each_tuple)):
        try:
            each_tuple[i] = mapping[i][each_tuple[i]]
        except:
            mapping[i][each_tuple[i]] = random.randint(1,k)
            each_tuple[i] = mapping[i][each_tuple[i]]



for each_dict in mapping:
    
    for i in range(1,k+1):
        try:
            print i, (each_dict.values()).count(i)
        except:
            pass