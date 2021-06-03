# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 16:50:26 2021

@author: nusayer
"""

def romanToInt(s):
    d = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    if len(s)==1:
        print(d.get(s))
        #return d.get(s)
    sm = 0
    i = 0
    while i < len(s):
        if i+1 > len(s)-1:
            sm += d.get(s[i])
            print(sm)
            return
            #return sm
        if d.get(s[i]) >= d.get(s[i+1]):
            sm += d.get(s[i])
            if i+1 == len(s)-1:
                sm += d.get(s[i+1])
                i+=1
            i+=1
        else:
            sm += d.get(s[i+1]) - d.get(s[i])
            i+=2
    print(sm)
    #return sm
            
    
romanToInt("LII")