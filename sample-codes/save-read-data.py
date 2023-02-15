#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Feb. 15, 2023

Data file format comparison
"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
from numpy import arange
import os
import time
import multiprocessing
from multiprocessing import Pool
import pandas as pd
import feather
import numpy as np
import pandas as pd
from scipy.integrate import odeint


########################################################################################################################
def save_data(format):
    np.random.seed = 42
    df_size = 10**7

    df = pd.DataFrame({
        'a': np.random.rand(df_size),
        'b': np.random.rand(df_size),
        'c': np.random.rand(df_size),
        'd': np.random.rand(df_size),
        'e': np.random.rand(df_size)
    })
    df.head()

    if format == "feather":
        fname = "sample-data.feather"
        df.to_feather(fname)
    elif format == "csv":
        fname = "sample-data.csv"
        df.to_csv(fname)
    else:
        pass


########################################################################################################################

def read_data(format):

    if format == "feather":
        fname = "sample-data.feather"
        df = pd.read_feather(fname)
        file_stats = os.stat(fname)
        print(f'feather datafile Size is {round(file_stats.st_size / (1024 * 1024))} MB')
        os.remove(fname)
        print("feather datafile removed")



    elif format == "csv":
        fname = "sample-data.csv"
        df = pd.read_csv(fname)
        file_stats = os.stat(fname)
        print(f'\ncsv datafile Size is {round(file_stats.st_size / (1024 * 1024), 3)} MB')
        os.remove(fname)
        print("csv datafile removed")
    else:
        pass

########################################################################################################################


def main():
    start = time.time()
    format = "feather"
    save_data(format=format)
    read_data(format=format)

    end = time.time()
    total_time = end-start
    print(f'Time to save and read a 10M by 4 datafile in the feather format: {round(total_time,3)} seconds')

    start = time.time()
    format = "csv"
    save_data(format=format)
    read_data(format=format)
    end = time.time()
    total_time = end - start
    print(f'Time to save and read a 10M by 4 datafile in the csv format: {round(total_time,3)} seconds')
########################################################################################################################


if __name__ == "__main__":
    main()
