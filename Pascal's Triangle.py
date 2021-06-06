# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 13:13:31 2021

@author: nusayer
"""

def generate(numRows):
    ls=[]
    if numRows == 1:
        ls.append([1])
        print(ls)
        return
    elif numRows == 2:
        ls.append([1])
        ls.append([1,1])
        print(ls)
        return
    ls = [[1],[1,1]]
    for i in range(2,numRows):
        templs = [1]
        last = ls[len(ls)-1]

        for j in range(len(last)-1):
            templs.append(last[j]+last[j+1])
        templs.append(1)
        ls.append(templs)
    print(ls)
    
generate(6)        