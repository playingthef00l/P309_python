#slr.py
# We're going to apply linear regression to each falling/rising segment.
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pwlf

# load in a clean drop as a dataframe:

df = pd.read_csv('~/fall_20/lab/oildrops/clean/d12.csv', sep=',')

x = np.array(df['frame'])
y = np.array(df['y'])

#This is the number of segments you found with seg_count
#The larger this number, the slower this program: patience is a virtue
seg_count = 3

#########Segmented Linear Regression

slr = pwlf.PiecewiseLinFit(x, y)
breaks = slr.fit(seg_count)
slopes = slr.calc_slopes()

##########Plot of the SLR

x_hat = np.linspace(x.min(), x.max(), 100)
y_hat = slr.predict(x_hat)

plt.figure()
plt.plot(x, y, 'o')
plt.plot(x_hat, y_hat, '-')
plt.show()

########## Calculating velocities
#Slopes are the rising/falling velocities.
# Average each respectively, and note for each drop:

v_rise = [x for x in slopes if x >= 0]
v_rise_avg = sum(v_rise)/len(v_rise)

v_fall = [x for x in slopes if x < 0]
v_fall_avg = sum(v_fall)/len(v_fall)

print(v_rise_avg, v_fall_avg)


