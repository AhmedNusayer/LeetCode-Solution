# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 21:55:21 2021

@author: nusayer
"""

import math

def isPerfectSquare(num):
    start = 0
    end = num
    while start <= end:
        mid = math.ceil((start + end)/2)
        sq = mid*mid
        if sq == num:
            print(mid)
            return True
        elif num < sq:
            end = mid - 1
        else:
            start = mid + 1
    return False
            

isPerfectSquare(14)