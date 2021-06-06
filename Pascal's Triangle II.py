# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 15:15:03 2021

@author: nusayer
"""

def getRow(rowIndex):
    ls=[]
    if rowIndex == 0:
        ls.append(1)
        print(ls)
        return
    elif rowIndex == 1:
        ls.append(1)
        ls.append(1)
        print(ls)
        return
    ls = [[1],[1,1]]
    for i in range(1,rowIndex):
        templs = [1]
        last = ls[len(ls)-1]

        for j in range(len(last)-1):
            templs.append(last[j]+last[j+1])
        templs.append(1)
        ls.append(templs)
    print(ls[len(ls)-1])
    
getRow(6)