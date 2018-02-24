# -*- coding:utf-8 -*-
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsLength = len(nums)
        if numsLength == 0:
            return 0
        i = 0
        j = 1
        while j < numsLength:
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1
