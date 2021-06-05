# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 01:46:12 2021

@author: nusayer
"""

def singleNumber(nums):
    from collections import Counter
    cnt = Counter(nums)
    for key,value in cnt.items():
        if value == 1:
            print(key)
    
singleNumber([1])