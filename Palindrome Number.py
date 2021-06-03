# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 16:51:55 2021

@author: Administrator
"""

def isPalindrome(x):
    x = str(x)
    i=0
    j=len(x)-1
    while(i!=j):
        if x[i] != x[j]:
            print("f")
            return False
        if j-i == 1:
            return True
        i+=1
        j-=1
    print("t")
    return True



isPalindrome(11)