# -*-coding:utf-8 -*-
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            if sum > 0:
                sum += nums[i]
            else:
                sum = nums[i]
            max_sum = max(sum, max_sum)
        return max_sum
