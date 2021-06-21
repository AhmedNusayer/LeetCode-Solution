# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 00:44:34 2021

@author: nusayer
"""

def isValid(s):
    if len(s) == 1:
        print("false")
        return False
    else:
        s2 = [s[0]]
        for i in range(1,len(s)):
            if len(s2) == 0:
                s2.append(s[i])
                continue
            if s2[len(s2)-1]+s[i] == "()" or s2[len(s2)-1]+s[i] == "{}" or s2[len(s2)-1]+s[i] == "[]":
                s2.pop()
            else:
                s2.append(s[i])
        if len(s2) == 0:
            print("true")
            return True
        else:
            print("false")
            return False
        
isValid("{[(){(])}]}")
            
            