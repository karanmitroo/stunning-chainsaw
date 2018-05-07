# from utils.numerical import numerical_dist
from utils.binning import binning
import numpy

# data = numpy.loadtxt("datasets/tae.csv", delimiter=",", usecols = (0,1,2,3))
data = numpy.loadtxt("datasets/congressional_voting_records.csv", delimiter=",", dtype=str)

categorical = data[:, :]
k = 2

categorical = binning(k, categorical)

# print categorical