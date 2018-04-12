import numpy as np

import pandas as pd


def run_avg(data, width):
    output = []
    for i in range(0,(len(data)-width+1)):
        segment = np.mean(data[i:width-1+i])
        output.append(segment)
        i += 1
    return output
 
