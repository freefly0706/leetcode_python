# -*- coding:utf-8 -*-
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        i = 0
        while i < nums_len:
            num = nums[i]
            if 0 < num <= nums_len and nums[num - 1] != num:
                nums[i] = nums[num - 1]
                nums[num - 1] = num
            else:
                i += 1
        i = 0
        while i < nums_len:
            if nums[i] != i + 1:
                break
            i += 1
        return i + 1
