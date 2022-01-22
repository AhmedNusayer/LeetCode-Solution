# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 21:39:58 2022

@author: nusayer
"""


def searchFirstElement(nums, target, start, end):
    first_element_index = end + 1
    temp = end + 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            if mid < first_element_index:
                first_element_index = mid
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    if first_element_index == temp:
        return -1
    return first_element_index
    
def searchLastElement(nums, target, start, end):
    last_element_index = -1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            if mid > last_element_index:
                last_element_index = mid
        if nums[mid] > target:
            end =  mid - 1
        else:
            start = mid + 1
    return last_element_index
    

def searchRange(nums, target):
    start = 0
    end = len(nums) - 1
    
    first_index = searchFirstElement(nums, target, start, end)
    last_index = searchLastElement(nums, target, start, end)
    
    print(first_index, last_index)
    

searchRange([5,7,7,8,8,8,8,8,8,8,10],8)
searchRange([5,7,7,8,8,10],8)
searchRange([],8)
        