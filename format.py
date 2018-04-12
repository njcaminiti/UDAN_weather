import numpy as np
import pandas as pd

# Reading the data from the CSV file that our SQL query generated into a Pandas DataFrame
raw = pd.read_csv('RESULTS.csv')

# Reshaping the Dataframe and trimming the start and end years where data is missing 
tidy = pd.pivot_table(raw, values = 'avg_temp', index= 'year', columns= 'city').loc[1750:2013]




