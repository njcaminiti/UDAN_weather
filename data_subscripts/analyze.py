import numpy as np
import pandas as pd


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

local_avg_10 = run_avg(tidy['Baltimore'], 10)
global_avg_10 = run_avg(tidy['global'], 10)

tidy.loc[:, 'Balt_avg'] = local_avg_10
tidy.loc[:, 'global_avg'] = global_avg_10