# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 16:00:47 2018

@author: Nicholas Caminiti
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Reading the data from the CSV file that our SQL query generated into a Pandas DataFrame
raw = pd.read_csv('data_subscripts/RESULTS.csv')

# Reshaping the Dataframe and trimming the start and end years where data is missing
tidy = pd.pivot_table(raw, values = 'avg_temp', index= 'year', columns= 'city').loc[1750:2013]

#check for and locate missing values
print(tidy.isnull().any())
print(tidy[tidy.isnull().any(axis=1)])

#impute missing value
tidy.loc[1780]['Baltimore'] = tidy.loc[1778]['Baltimore']



# Returns running average of a series over a user defined width (as ndarray)
# Backfills with first calculation so output data matches length of input data.
def run_avg(data, width, bfill = True):
    output = []
    if width > len(data)/2:
        return print("Width too large. Please select a value less than " \
                     + str(len(data)/4) + ".")
            #^^^ This is a safeguard against selecting a range that is too large.
    for i in range(0,(len(data))):
        if i < width-1:
            if bfill:
                output.append(round(np.mean(data[0:width-1]), 2))
            # Backfills with first calculation so output data matches length of input data.
            continue
        else:
            output.append(round(np.mean(data[i-width+1:i]), 2))
    return np.array(output)


#Compute moving averages
local_avg_10 = run_avg(tidy['Baltimore'], 10)
global_avg_10 = run_avg(tidy['global'], 10)

#append moving averages to existing dataframe
tidy.loc[:, 'Balt_avg'] = local_avg_10
tidy.loc[:, 'global_avg'] = global_avg_10

#compare our datasets
tidy.plot(subplots=True, lw=2, title='Smoothed vs Unsmoothed trendlines')
tidy[['Balt_avg','global_avg']].plot(lw=4, title='Temperature 1750-2013 (10-year moving avg)').set_ylabel('Temperature')

#lines of best fit (slope, y-intercept)
mbalt, bbalt = np.polyfit(tidy.index, tidy['Balt_avg'], 1)
mglob, bglob = np.polyfit(tidy.index, tidy['global_avg'], 1)

plt.plot(tidy.index, tidy['global_avg'], tidy.index, mglob*tidy.index+bglob, label='global', lw=2)
plt.plot(tidy.index, tidy['Balt_avg'], tidy.index, mbalt*tidy.index+bbalt, label='Baltimore', lw=2)
plt.show()
