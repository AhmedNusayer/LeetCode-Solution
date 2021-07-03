# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 13:23:40 2021

@author: nusayer
"""

def mySqrt(x):
    i = 0
    j = 1
    while 1:
        ans1 = i*i
        ans2 = j*j
        if ans1 == x:
            print(i)
            return i
        elif ans2 == x:
            print(j)
            return j
        elif x > ans1 and x < ans2:
            print(i)
            return i
        i+=1
        j+=1
        
mySqrt(8)