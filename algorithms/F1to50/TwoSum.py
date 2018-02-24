# -*- coding: UTF-8 -*-
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        elements = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if key in elements:
                return [elements.get(key), i]
            else:
                elements[nums[i]] = i
        return None
