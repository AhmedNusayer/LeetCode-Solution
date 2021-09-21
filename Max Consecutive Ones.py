# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:19:46 2021

@author: nusayer
"""

def findMaxConsecutiveOnes(nums):
    i = 0
    mx = 0
    temp = 0
    while i < len(nums):
        if nums[i] == 0:
            i+=1
            continue
        else:
            while nums[i] == 1:
                temp += 1
                i+=1
                if i == len(nums):
                    break
            mx = max(mx, temp)
            temp = 0
    print(mx)
    return mx

findMaxConsecutiveOnes([1,0,1,1,0,1])