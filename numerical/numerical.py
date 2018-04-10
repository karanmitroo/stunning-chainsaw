import numpy
import random
a = []


for i in range(100):
    a.append(random.randint(1,10))
print a
mean = numpy.mean(a)
std_dev = numpy.std(a)
