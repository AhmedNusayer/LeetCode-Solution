# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 20:44:34 2021

@author: nusayer
"""
import math

def intersection(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    if n1 < n2:
        sm = nums1
        lg = nums2
    else:
        sm = nums2
        lg = nums1
    
    lg.sort()
    ls = []
    
    for i in range(len(sm)):
        if sm[i] in ls:
            i+=1
            continue
        start = 0
        end = len(lg) - 1
        while start <= end:
            mid = math.ceil((start+end)/2)
            if sm[i] == lg[mid]:
                ls.append(sm[i])
                break
            if sm[i] < lg[mid]:
                end = mid - 1
            else:
                start = mid + 1
    
    print(ls)
        
            
    

intersection([4,9,5], [9,4,9,8,4])