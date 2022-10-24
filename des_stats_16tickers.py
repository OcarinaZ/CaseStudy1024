#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
#%%

def des_stats(path):
    
    prices = pd.read_csv(path,index_col=0)
    
    def total_return(x):
        
        t = x.dropna()
        total_return = t[-1]/t[0]-1 
        return total_return
    
    # Since price time series are unlikely to be normally distributed, 
    # here I didn't calculate skewness and kurtosis - maybe they're more suitable 
    # for return time series.
    des_table = prices.agg(['min','max','mean','std',total_return]).T

    return des_table