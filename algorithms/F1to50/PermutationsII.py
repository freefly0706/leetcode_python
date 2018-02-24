# -*-coding:utf-8 -*-
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.back_tracking(res, [], nums, [False] * len(nums))
        return res

    def back_tracking(self, res, permutation, nums, has_included):
        if len(permutation) == len(nums):
            res.append(permutation.copy())
            return
        i = 0
        while i < len(nums):
            if not has_included[i]:
                permutation.append(nums[i])
                has_included[i] = True
                self.back_tracking(res, permutation, nums, has_included)
                permutation.pop()
                has_included[i] = False
                while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    i += 1
            i += 1
