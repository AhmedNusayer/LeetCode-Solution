# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 20:30:04 2021

@author: nusayer
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = None
        
    def mergeTwoLists(l1: ListNode, l2: ListNode):
        l = []
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                l.append(l1.val)
                l1 = l1.next
            else:
                l.append(l2.val)
                l2 = l2.next
        while l1 is not None:
            l.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            l.append(l2.val)
            l2 = l2.next
        
        if len(l) == 0:
            return l1
        for x in range(len(l)-1,-1,-1):
            ll = ListNode(l[x], self.head)
            self.head = ll
        
        print(ll)
        return ll