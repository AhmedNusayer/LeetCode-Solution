# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:48:14 2021

@author: nusayer
"""

def twoSum(numbers, target):
    i = 0
    j = len(numbers) - 1
    while 1:
        print("xxx")
        if numbers[i] + numbers[j] == target:
            print([i+1,j+1])
            return [i+1,j+1]
        elif numbers[i] + numbers[j] < target:
            i+=1
        else:
            j-=1
            
twoSum([-1,0], -1)