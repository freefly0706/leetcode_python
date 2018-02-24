# -*- coding:utf-8 -*-
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for element in nums:
            if element != val:
                nums[i] = element
                i += 1
        return i
