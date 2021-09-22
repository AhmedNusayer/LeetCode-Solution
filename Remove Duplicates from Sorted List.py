# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:15:42 2021

@author: nusayer
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.realHead = None
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        l = []
        while head is not None:
            temp = head.val
            l.append(temp)
            head = head.next
            while head is not None and head.val == temp:
                head = head.next
         
        if len(l) == 0:
            return head
        
        for i in range(len(l)-1,-1,-1):
            ll = ListNode(l[i], self.realHead)
            self.realHead = ll            
        
        print(ll)
        return ll