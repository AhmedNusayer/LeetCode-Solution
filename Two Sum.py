# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 15:36:53 2021

@author: Administrator
"""

def twoSum(nums, target):
    sortedNum = sorted(nums)
    i=0
    j=len(nums)-1
    while(i!=j):
        if sortedNum[i]+sortedNum[j] == target:
            idx1 = nums.index(sortedNum[i])
            idx2 = nums.index(sortedNum[j])
            if idx1 == idx2:
                temp = sortedNum[j]
                nums[nums.index(sortedNum[j])] = 0
                idx2 = nums.index(temp) 
            print([idx1, idx2])
            return
        elif sortedNum[i]+sortedNum[j] > target:
            j-=1
        else:
            i+=1
    
twoSum([3,3],6)