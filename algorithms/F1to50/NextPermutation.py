# -*-coding:utf-8 -*-
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numsLength = len(nums)
        pos = numsLength - 1
        while pos > 0 and nums[pos] <= nums[pos - 1]:
            pos -= 1
        if pos:
            exchangeIndex = numsLength - 1
            while nums[exchangeIndex] <= nums[pos - 1]:
                exchangeIndex -= 1
            nums[pos - 1], nums[exchangeIndex] = nums[exchangeIndex], nums[pos - 1]
        for i in range((numsLength - pos) // 2):
            nums[pos + i], nums[numsLength - 1 - i] = nums[numsLength - 1 - i], nums[pos + i]
