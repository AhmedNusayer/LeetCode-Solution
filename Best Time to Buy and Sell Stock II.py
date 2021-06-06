# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 18:23:44 2021

@author: nusayer
"""

def maxProfit(prices):
        mm = prices[0]
        mx = prices[0]
        maxProf = mx-mm
        if len(prices) == 1:
            print(maxProf)
            return
        for i in range(len(prices)):
            if prices[i]<mm:
                mm = prices[i]
            mx = prices[i]
            if mx-mm+maxProf > maxProf:
                maxProf += mx-mm
                mm=mx
        print(maxProf)
        
maxProfit([7,1,5,3,6,4])