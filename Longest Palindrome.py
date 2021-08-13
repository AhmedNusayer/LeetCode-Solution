# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 16:32:10 2021

@author: nusayer
"""

from collections import Counter

def longestPalindrome(s):
    res = Counter(s)
    ans = 0
    flag = 0
    for key in res:
        if res.get(key) % 2 == 0:
            ans += res.get(key)
        else:
            if flag == 0:
                ans += res.get(key)
                flag = 1
            else:
                ans += res.get(key)-1
            
    print(ans)
    return ans

longestPalindrome("abccccdd")
    