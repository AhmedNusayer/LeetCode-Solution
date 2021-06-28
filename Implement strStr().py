# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 23:09:50 2021

@author: nusayer
"""

def strStr(haystack, needle):
    if len(needle) == 0:
        print(0)
        return 0
    j = 0
    flag = 0
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i] == needle[0]:
            if len(needle) == 1:
                print(i)
                return i
            k = i+1
            for j in range(1,len(needle)):
                if haystack[k] != needle[j]:
                    flag = 1
                    break
                k+=1
            if flag == 0:
                print(i)
                return i
            k+=1
        flag = 0
    print(-1)
    return -1

strStr("hello", "ll")
            