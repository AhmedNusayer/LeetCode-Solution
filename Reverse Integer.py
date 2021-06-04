# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:09:54 2021

@author: nusayer
"""
def reverse(x):
    mm = -2147483648
    mx = 2147483647
    x = str(x)
    if x[0] == "-":
        ans = "-"
    else:
        ans = ""
    for i in range(len(x)-1, -1, -1):
        if x[i] != "-":
            ans += x[i]
    if int(ans) >= mm and int(ans) <= mx:
        print(int(ans))
    else:
        print(0)
    
    
reverse(2147483641)