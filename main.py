# from utils.numerical import numerical_dist
from utils.binning import binning


data = numpy.loadtxt("datasets/tae.csv", delimiter=",", usecols = (0,1,2,3))

categorical = data[:, (1,2)]
k = 3

categorical = binning(k, categorical)