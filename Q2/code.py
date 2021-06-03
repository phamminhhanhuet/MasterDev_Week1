# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 10:32:22 2021

@author: Admin
"""
from collections import defaultdict
from typing import List
import time
import csv
from random import *
from pandas import set_option
from pandas import read_csv
from matplotlib import pyplot as plt
from scipy import stats
import numpy as np

#give a non-empty array of integers nums, every element appear twice except one. Find that single one.
# must implement a soluction with a liinear rutinom complexity and use only constant extra space

#constraint
# 1 <= num.length <= 3 * 10 ^ 4
# - 3 * 10^4 <= num[i] <= 3 * 10^4

class Solution(object):
    def singleNumber(self, nums):
        """
        Parameters
        ----------
        nums : List[int]
        Returns
        -------
        int
        """
        return 2 * sum(set(nums)) - sum(nums)
        
    #method2
    def singleNumber1(self, nums):
        new_list = []
        for i in nums:
            if i not in new_list:
                new_list.append(i)
            else:
                new_list.remove(i)
        return new_list

        # method 3
    
    def singleNumber2(self, nums: List[int]) :
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
            
        for i in hash_table:
            if hash_table[i] ==1:
                return i
            #method 4
            
    def singleNumber3(self, nums):
        """
        find the unique values by xor 
        """
        ir = 0
        for i in nums:
            ir^= i
        return ir
    
    def statistic_report(self, samples):
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
        plt.figure()
        plt.hist(samples)
        plt.show()
    
    
def radom_samples():
    n = randint(1, 50)
    if n % 2 ==0:
        n += 1
    unique = randint(1, n)
    count = 0
    samples = []
    for x in range(n):
        if x != unique:
            if count % 2 == 0:
                samples.append(x)
            else:
                samples.append(samples[count-1])
            count += 1
    samples.append(unique)
    return samples

def run_statistic(method):
    time_list = []
    
    solution = Solution()
    for i in range(1000):
        start = time.time()
        samples = radom_samples()
       
        if(method == 0):
            print(solution.singleNumber(samples))
        elif (method ==1):
            print(solution.singleNumber1(samples))
        elif( method ==2):
            print(solution.singleNumber2(samples))
        elif(method ==3):
            print(solution.singleNumber3(samples)) 
        
        end = time.time()
        time_list.append((time.time() - start) * 1000)     
    solution.statistic_report(time_list)


if __name__ == "__main__":
    run_statistic(0)
    run_statistic(1)
    run_statistic(2)
    run_statistic(3)
        
    
        

    
    
    
            