# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 22:01:10 2021

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
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = []
        n2 = []
        while l1 is not None:
            n1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            n2.append(l2.val)
            l2 = l2.next
        num1 = ""
        num2 = ""
        for i in range(len(n1)-1,-1,-1):
            num1 += str(n1[i])
        for j in range(len(n2)-1,-1,-1):
            num2 += str(n2[j])
            
        ans = str(int(num1) + int(num2))
        
        for k in range(len(ans)):
            node = ListNode(ans[k], self.head)
            print(node)
            self.head = node
            
        print(node)
        
        return node
    
            
