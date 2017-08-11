# -*- coding: UTF-8 -*-
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c1 = l1
        c2 = l2
        temp = ListNode(0)
        result = temp
        sumtemp = 0
        while (c1 is not None) or (c2 is not None):
            sumtemp //= 10
            if c1 is not None:
                sumtemp += c1.val
                c1 = c1.next
            if c2 is not None:
                sumtemp += c2.val
                c2 = c2.next
            temp.next = ListNode(sumtemp % 10)
            temp = temp.next
        if sumtemp // 10 == 1:
            temp.next = ListNode(1)
        return result.next
