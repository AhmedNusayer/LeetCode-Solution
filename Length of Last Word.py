# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 21:04:01 2021

@author: nusayer
"""

def lengthOfLastWord(s):
    cnt = 0
    x = 0
    flag = 0
    for j in range(len(s)-1,-1,-1):
        if s[j] == " " and flag == 0:
            x+=1
        else:
            flag = 1
    for i in range(len(s)-1-x,-1,-1):
        if s[i] != " ":
            cnt += 1
        else:
            break
        
    print(cnt)
    return cnt
        
lengthOfLastWord("hello worlds   ")