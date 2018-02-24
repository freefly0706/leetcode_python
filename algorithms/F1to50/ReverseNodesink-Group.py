# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 1:
            return head
        res = ListNode(0)
        res.next = head
        p = res
        q = p
        while True:
            count = 0
            while count < k:
                if p.next:
                    p = p.next
                    count += 1
                else:
                    return res.next
            q1 = q.next
            p1 = q1.next
            pNext = p.next
            while p1 != pNext:
                tmp = p1.next
                q1.next = tmp
                p1.next = q.next
                q.next = p1
                p1 = tmp
            q = q1
            p = q
