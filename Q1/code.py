# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 10:18:38 2021

@author: Admin
"""

from random import *
from math import sqrt
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

# estimate pi number
# monte carlo simulation

def estimate_pi():
    samples =[]
    for i in range(35):
        inside = 0
        n_points = 1000
        
        for i in range(0,n_points):
            x = random()
            y = random()
            if (sqrt(x*x + y*y) <=1):
                inside +=1 
                
        pi =4 *inside/ n_points
        print(pi)
        samples.append(pi)
    statistic_report(samples)
    
def statistic_report(samples):
    print("Mean = {:.4f}".format(np.mean(samples)))
    print("Variance = {:.4f}".format(np.var(samples)))
    print("Std = {:.4f}".format(np.std(samples)))
    print(stats.mode(samples))
    print("Median = {:.4f}".format(np.median(samples)))
    print("Min = {:.4f}".format(np.min(samples)))
    print("Max = {:.4f}".format(np.max(samples)))
    print("Q1 = {:.4f}".format(np.quantile(samples, 0.25)))
    print("Q2 = {:.4f}".format(np.quantile(samples, 0.5)))
    print("Q3 = {:.4f}".format(np.quantile(samples, 0.75)))
    plt.hist(samples)
    plt.show()
    
if __name__ == "__main__":
    estimate_pi()





