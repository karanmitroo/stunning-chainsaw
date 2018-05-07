import numpy
import random
from math import sqrt

def z_score_norm(num, mean, std_dev):
    return (num - mean) / std_dev

def numerical_dist(x, y, numerical):
    mean = []
    std_dev = []

    #Calculating the mean and the standard deviation for the numerical attributes
    for i in range(len(numerical[0])):
        mean.append(numpy.mean(numerical[:, i]))
        std_dev.append(numpy.std(numerical[:, i]))

    #Calculating the z_scores for all the numerical values.
    z_scores = []
    for i in range(0, len(numerical)):
        z_scores.append([])
        for j in range(len(numerical[i])):
            z_scores[i].append(z_score_norm(numerical[i][j], mean[j], std_dev[j]))

    total = 0
    for i in range(len(z_scores[0])):
        total += pow(abs(z_scores[x][i] - z_scores[y][i]), 2)
        
    return sqrt(total)


