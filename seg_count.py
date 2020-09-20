#!/bin/python3
# segment_count.py
# count the number of rising/falling segments for each drop - with your eyes

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('~/fall_20/lab/oildrops/raw/d1.csv', sep=',')

x = df['frame']
y = df['y']

plt.scatter(x,y)
plt.show()
