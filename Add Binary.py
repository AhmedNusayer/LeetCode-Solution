# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 16:19:51 2021

@author: nusayer
"""

def addBinary(a, b):
    carry = 0
    ans = ""
    lena = len(a)
    lenb = len(b)
    temp = ""
    if lena > lenb:
        for x in range(lena-lenb):
            temp += "0"
        b = temp + b
    elif lenb > lena:
        for x in range(lenb-lena):
            temp += "0"
        a = temp + a
    print(a)
    print(b)
    for i in range(len(a)-1,-1,-1):
        sm = int(a[i]) + int(b[i]) + carry
        if sm == 0:
            ans += "0"
            carry = 0
        elif sm == 1:
            ans += "1"
            carry = 0
        elif sm == 2:
            ans += "0"
            carry = 1
        else:
            ans += "1"
            carry = 1
    if carry == 1:
        ans = ans + str(carry)
        print(ans[::-1])
        return ans[::-1]
    else:
        print(ans[::-1])
        return ans[::-1]
    
addBinary("101111", "10")
    