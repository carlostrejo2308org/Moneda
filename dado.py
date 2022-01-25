from random import randint
import numpy

def dice():
    return numpy.random.choice(numpy.arange(0, 6), p=[0.14, 0.14, 0.14, 0.14, 0.3, 0.14])


results = [0]*6
for i in range(200):
    results[dice()] += 1
print(results)
