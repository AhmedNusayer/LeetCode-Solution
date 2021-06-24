# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 17:50:44 2021

@author: nusayer
"""


def longestCommonPrefix(strs):
    s = ""
    if len(strs) == 1:
        print(strs[0])
        return strs[0]
    minString = min(strs, key=len)
    minStringLen = len(minString)
    j=0
    for k in range(minStringLen):
        flag=1
        i = 0
        while i < len(strs)-1:
            if strs[i][j] != strs[i+1][j]:
                flag = 0
                break
            i+=1 
        
        if flag == 1:
            s += strs[0][j]
        else:
            break
        j+=1
    print(s)
    return s
    
longestCommonPrefix(["flower","flow","flight"])