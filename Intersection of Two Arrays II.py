# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 19:00:46 2021

@author: nusayer
"""

from collections import Counter
import math

def intersect(nums1, nums2):
    c1 = Counter(nums1)
    c2 = Counter(nums2)
    final = []
    print(c1)
    print(c2)
    
    c1Keys = list(c1.keys())
    c2Keys = list(c2.keys())
    
    c2Keys.sort()
    for key in c1Keys:
        start = 0
        end = len(c2Keys) - 1
        while start <= end:
            mid = math.ceil((start+end)/2)
            
            if key == c2Keys[mid]:
                final.append(key)
                break
            elif key < c2Keys[mid]:
                end = mid - 1
            else:
                start = mid + 1
                
    print(final)
    
    ans = []
    for i in range(len(final)):
        x = c1.get(final[i])
        y = c2.get(final[i])
        for j in range(min(x , y)):
            ans.append(final[i])
            
    print(ans)
        

intersect([1,2,2,1], [2,2])
