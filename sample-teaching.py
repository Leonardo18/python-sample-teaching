import pandas as pd
import numpy as np
from math import ceil


population = 150
sample = 15
k = ceil(population / sample)


print(k)


r = np.random.randint(low=1, high=k + 1, size=1)

acumulator = r[0]


sorted = []


for i in range(sample):
    sorted.append(acumulator)
    acumulator += k


print(sorted)

base = pd.read_csv('iris.csv')


final_base = base.loc[sorted]


print(final_base)