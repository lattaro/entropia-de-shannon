
import pandas as pd
from scipy.stats import entropy
import numpy as np
import random

e = 0.5
pop_inicial=[]

tam_pop_inicial = 3
x = random.uniform(0, 1)
pop_inicial.append(x)

while len(pop_inicial) <= tam_pop_inicial:
    x = random.uniform(0, 1)
    pop_inicial.append(x)
    entropia = entropy(pop_inicial)
    if entropia < e:
        del(pop_inicial[-1])
print('pop_inicial: ',pop_inicial)
print('entropia: ',entropia)