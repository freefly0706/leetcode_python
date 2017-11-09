# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        newListNode = ListNode(0)
        swapedHead = newListNode
        q = head
        p = head.next
        while q and p:
            newListNode.next = p
            q.next = p.next
            p.next = q
            newListNode = q
            q = q.next
            if not q:
                break
            p = q.next
        return swapedHead.next
