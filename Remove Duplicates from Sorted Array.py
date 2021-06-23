# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 13:02:28 2021

@author: nusayer
"""

def removeDuplicates(nums):
    i = 1
    if len(nums) > 0:
        mx = nums[0]
        x = nums[len(nums)-1]
    while i < len(nums):
        if nums[i] > mx:
            mx = nums[i]
            i+=1
            continue
        for j in range(i,len(nums)):
            if nums[j] > mx:
                mx = nums[j]
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                break
        if nums[i] == x:
            break
        i+=1
    cnt = 0
    for k in range(0,len(nums)):
        cnt+=1
        if nums[k] == x:
            break
    print(cnt)
    print(nums)
    return cnt

removeDuplicates([1,1,1,2,3])
            
    