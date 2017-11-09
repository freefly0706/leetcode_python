# -*- coding:utf-8 -*-
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists is None:
            return None

        def mergeSort(low, high):
            if low < high:
                mid = (low + high) // 2
                left = mergeSort(low, mid)
                right = mergeSort(mid + 1, high)
                return mergeTwoLists(left, right)
            else:
                return lists[low]

        def mergeTwoLists(l1, l2):
            head = ListNode(0)
            p = head
            while l1 and l2:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
            if l1:
                p.next = l1
            if l2:
                p.next = l2
            return head.next

        return mergeSort(0, len(lists) - 1)
