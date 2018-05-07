from utils.numerical import numerical_dist
from utils.binning import binning
from utils.kmeans import k_means
import numpy

data = numpy.loadtxt("datasets/stocks.csv", delimiter=",",dtype = str)
# data = numpy.loadtxt("datasets/congressional_voting_records.csv", delimiter=",", dtype=str)

categorical = data[:, (0,2,3)]
numerical = data[:, (1, 4)].astype(numpy.float)
k = 3

categorical = binning(k, categorical)

# print categorical
# print numerical_dist(11, 12, numerical)

labels = k_means(k, categorical)

print labels
# for i in range(k):
#     try:
#         print i, labels.count(i)
#     except:
#         print i, 0