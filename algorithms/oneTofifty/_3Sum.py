# -*- coding: UTF-8 -*-
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        positiveLowBound = 0
        while positiveLowBound < len(nums) and nums[positiveLowBound] <= 0:
            positiveLowBound += 1
        for i in range(positiveLowBound):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            low = i + 1
            high = len(nums) - 1
            while low < high:
                sums = nums[i] + nums[low] + nums[high]
                if sums == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low + 1] == nums[low]:
                        low += 1
                    while low < high and nums[high - 1] == nums[high]:
                        high -= 1
                    low += 1
                    high -= 1
                elif sums < 0:
                    low += 1
                else:
                    high -= 1
        return res
