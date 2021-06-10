# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 18:31:46 2021

@author: nusayer
"""

def isPalindrome(s):
    i=0
    j=len(s)-1
    flag = 0
    while True:
        while ord(s[i]) < 48 or (ord(s[i]) > 57 and ord(s[i]) < 65) or (ord(s[i]) > 90 and ord(s[i]) < 97) or ord(s[i]) > 122 :
            i+=1
            if i==j or i>j:
                break
        while ord(s[j]) < 48 or (ord(s[j]) > 57 and ord(s[j]) < 65) or (ord(s[j]) > 90 and ord(s[j]) < 97) or ord(s[j]) > 122 :
            j-=1
            if i==j or i>j:
                break
        if i==j or i>j:
            break
        else:
            if ((ord(s[i]) > 47 and ord(s[i])<58) and (ord(s[j]) > 64 and ord(s[j])<91)) or ((ord(s[j]) > 47 and ord(s[j])<58) and (ord(s[i]) > 64 and ord(s[i])<91)):
                flag=1
                break
            elif s[i] != s[j] and ord(s[i])+32 != ord(s[j]) and ord(s[i])-32 != ord(s[j]):
                flag = 1
                break
        i+=1
        j-=1
        if i>j:
            break
    if flag == 0:
        print("true")
        return True
    elif flag == 1:
        print("false")
        return False
    
isPalindrome("A man, a plan, a canal: Panama")