# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 21:49:10 2021

@author: nusayer
"""

def plusOne(digits):
    length = len(digits)
    carry = 0
    if digits[length-1] != 9:
        digits[length-1] += 1
    else:
        digits[length-1] = 0
        carry = 1
    for i in range(length-2,-1,-1):
        if carry == 0:
            break
        else:
            if digits[i] != 9:
                digits[i] += 1
                carry = 0
            else:
                digits[i] = 0
                carry = 1
    if carry == 1:
        digits[0] = 1
        for x in range(1,length):
            digits[x] = 0
        digits.append(0)
    print(digits)
    return digits

plusOne([9,9,9])
            