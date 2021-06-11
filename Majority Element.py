# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 00:30:25 2021

@author: nusayer
"""

def majorityElement(nums):
    from collections import Counter
    cnt = Counter(nums)
    print(cnt.most_common()[0][0])
    
majorityElement([2,3,4,3,4,4,4,4,4,1,2,3,1])