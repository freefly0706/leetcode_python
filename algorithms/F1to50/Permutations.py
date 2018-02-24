# -*-coding:utf-8 -*-
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.back_tracking(res, [], nums, [False] * len(nums))
        return res

    def back_tracking(self, res, permutation, nums, has_included):
        if len(permutation) == len(nums):
            res.append(permutation.copy())
            return
        for i in range(len(nums)):
            if not has_included[i]:
                permutation.append(nums[i])
                has_included[i] = True
                self.back_tracking(res, permutation, nums, has_included)
                permutation.pop()
                has_included[i] = False
