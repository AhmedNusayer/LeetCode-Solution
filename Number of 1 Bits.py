# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 19:32:04 2021

@author: nusayer
"""

def hammingWeight(n):
    c=0
    n = bin(n).replace("0b", "")
    ans = n.count("1")
    print(ans)
    return ans
    
hammingWeight(00000000000000000000000000001011)