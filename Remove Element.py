# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 12:06:56 2021

@author: nusayer
"""

def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] != val:
            i += 1
        else:
            flag = 0
            for j in range(i,len(nums)-1):
                if nums[j] != nums[j+1]:
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp
                    flag = 1
            if flag == 0:
                break
    cnt = 0
    for k in range(len(nums)-1,-1,-1):
        if nums[k] == val:
            cnt+=1
        else:
            break
    print(len(nums)-cnt)
    print(nums)
    return len(nums)-cnt


removeElement([0,1,2,2,3,0,4,2], 2)             
                
                
            