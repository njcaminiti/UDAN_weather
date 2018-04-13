import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tidy.plot(subplots=True, lw=2, title='Smoothed vs Unsmoothed trendlines')
tidy[['Balt_avg','global_avg']].plot(lw=4, title='Temperature 1750-2013 (10-year moving avg)').set_ylabel('Temperature')

#lines of best fit (slope, y-intercept)
mbalt, bbalt = np.polyfit(tidy.index, tidy['Balt_avg'], 1) 
mglob, bglob = np.polyfit(tidy.index, tidy['global_avg'], 1)

plt.plot(tidy.index, tidy['global_avg'], tidy.index, mglob*tidy.index+bglob, label='global', lw=2)
plt.plot(tidy.index, tidy['Balt_avg'], tidy.index, mbalt*tidy.index+bbalt, label='Baltimore', lw=2)
plt.show()








