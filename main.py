from utils.numerical import numerical_dist
from utils.binning import binning
from utils.kmeans import k_means
import numpy as np

#IRIS dataset
# data = np.loadtxt("datasets/iris.csv", delimiter=",", dtype=str)
# categorical = data[:, (4)]
# numerical = data[:, (0,1,2,3)].astype(np.float)
# k = 3
# categorical = binning(k, categorical)

#TEACHING ASSISTANT EVALUATION dataset
# data = np.loadtxt("datasets/tae.csv", delimiter=",", dtype=str)
# categorical = data[:, (1,2)]
# numerical = data[:, (0,3,4,5)].astype(np.float)
# k = 3
# categorical = binning(k, categorical)

#CREDIT APPROVAL dataset
# data = np.loadtxt("datasets/crx.csv", delimiter=",", dtype=str)
# categorical = data[:, (0,3,4,5,6,8,9,11,12)]
# numerical = data[:, (1,2,7,10,13,14)].astype(np.float)
# k = 2
# categorical = binning(k, categorical)

#ADULT dataset
# data = np.loadtxt("datasets/adult.csv", delimiter=",", dtype=str)
# categorical = data[:, (1,3,5,6,7,8,9,13)]
# numerical = data[:, (0,2,4,10,11,12)].astype(np.float)
# k = 2
# categorical = binning(k, categorical)

#QSAR BIODEGRADABLE dataset
# data = np.loadtxt("datasets/biodeg.csv", delimiter=";", dtype=str)
# categorical = data[:, (23,24,25,27,28,32,36,41)]
# numerical = data[:, (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,26,29,30,31,33,34,35,37,38,39,40)].astype(np.float)
# k = 2
# categorical = binning(k, categorical)

#CONTRACEPTIVE METHOD CHOICE dataset
"""
No need of binning in this dataset as categorical data already 
converted to numerical format. Also range of data values < k, so 
binning not to be done.
"""
data = np.loadtxt("datasets/biodeg.csv", delimiter=";", dtype=str)
categorical = data[:, (1,2,4,5,6,7,8,9)]
numerical = data[:, (0,3)].astype(np.float)
k = 3


#Making a combined array of categorical and numerical
total = np.concatenate([categorical, numerical], axis = 1)

#Getting results for different categories of data
labels_categorical = k_means(k, categorical)
labels_numerical = k_means(k, numerical)
labels_total = k_means(k, total)

print "Only Categorical result:", labels_categorical
print "Only numerical result:", labels_numerical
print "Mixed Result:", labels_total
