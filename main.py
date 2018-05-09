from utils.numerical import numerical_dist
from utils.binning import binning
from utils.kmeans import k_means
from utils.min_max_normalize import min_max_normalize
from clean_test import clean_file, clean_data
import numpy as np

#IRIS dataset
# data = np.loadtxt("datasets/iris.csv", delimiter=",", dtype=str)
# categorical = data[:, (4)]
# numerical = data[:, (0,1,2,3)].astype(np.float)
# k = 3
# categorical = binning(k, categorical)

#TEACHING ASSISTANT EVALUATION dataset
data = np.loadtxt("datasets/tae.csv", delimiter=",", dtype=str)
categorical = data[:, (1,2)]
numerical = data[:, (0,3,4)].astype(np.float)
k = 3
categorical = binning(k, categorical)
unique, counts = np.unique(data[:, (5)], return_counts = True)

#CREDIT APPROVAL dataset
# clean_file("datasets/crx.csv")
# data = np.loadtxt("datasets/crx_cleaned.csv", delimiter=",", dtype=str)
# categorical = data[:, (0,3,4,5,6,8,9,11,12)]
# numerical = data[:, (1,2,7,10,13,14)].astype(np.float)
# k = 2
# categorical = binning(k, categorical)
# unique, counts = np.unique(data[:, (15)], return_counts = True)


#ADULT dataset
# data = np.loadtxt("datasets/adult.csv", delimiter=",", dtype=str)
# categorical = data[:, (1,3,5,6,7,8,9,13)]
# numerical = data[:, (0,2,4,10,11,12)].astype(np.float)
# k = 2
# categorical = binning(k, categorical)
# unique, counts = np.unique(data[:, (14)], return_counts = True)


#QSAR BIODEGRADABLE dataset (Numerical data has a good impact over categorical)
# data = np.loadtxt("datasets/biodeg.csv", delimiter=";", dtype=str)
# categorical = data[:, (23,24,25,27,28,32,36)]
# numerical = data[:, (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,26,29,30,31,33,34,35,37,38,39,40)].astype(np.float)
# k = 2
# categorical = binning(k, categorical)
# unique, counts = np.unique(data[:, (41)], return_counts = True)


#CONTRACEPTIVE METHOD CHOICE dataset
"""
No need of binning in this dataset as categorical data already 
converted to numerical format. Also range of data values < k, so 
binning not to be done.
"""
# data = np.loadtxt("datasets/cmc.csv", delimiter=",", dtype=str)
# categorical = data[:, (1,2,4,5,6,7,8)]
# numerical = data[:, (0,3)].astype(np.float)
# k = 3
# unique, counts = np.unique(data[:, (9)], return_counts = True)


#STOCKS, a temp dataset
# data = np.loadtxt("datasets/stocks.csv", delimiter=",", dtype=str)
# categorical = data[:, (0,2,3)]
# numerical = data[:, (1,4)].astype(np.float)
# k = 4
# categorical = binning(k, categorical)


classes = dict(zip(unique, counts))
#Normalizing numerical data using min_max_normalizaion
numerical = min_max_normalize(k, numerical)

#Making a combined array of categorical and numerical
total = np.concatenate([categorical, numerical], axis = 1)

#Getting results for different categories of data
labels_categorical, inertia_categorical = k_means(k, categorical)
labels_numerical, inertia_numerical = k_means(k, numerical)
labels_total, inertia_total = k_means(k, total)

print "Only Categorical result:", labels_categorical, inertia_categorical
print "Only numerical result:", labels_numerical, inertia_numerical
print "Mixed Result:", labels_total, inertia_total

print classes