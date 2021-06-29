# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 21:51:33 2021

@author: nusayer
"""

def searchInsert(nums, target):
    import math
    i = 0
    j = len(nums)-1
    if i == j:
        if target <= nums[i]:
            print(i)
            return i
        elif target > nums[i]:
            print(i+1)
            return i+1
    
    while i <= j:
        if i+1 == j:
            if nums[i] == target:
                print(i)
                return i
            elif nums[j] == target:
                print(j)
                return j
            elif target > nums[i] and target > nums[j]:
                print(j+1)
                return j+1
            elif target > nums[i] and target < nums[j]:
                print(i+1)
                return i+1
            else:
                print(i)
                return i
        mid = math.floor((i+j)/2)
        if nums[mid] == target:
            print(mid)
            return mid
        elif target > nums[mid]:
            i = mid
        else:
            j = mid

        
searchInsert([1,3,5,10,11,12],8)