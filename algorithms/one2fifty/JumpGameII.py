# -*-coding:utf-8 -*-
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len <= 1:
            return 0
        index, jumps = 0, 1
        while index + nums[index] < nums_len - 1:
            jumps += 1
            farthest_index, farthest = 1, 1 + nums[index + 1]
            for i in range(2, nums[index] + 1):
                distance = i + nums[index + i]
                if distance > farthest:
                    farthest_index = i
                    farthest = distance
            index += farthest_index
        return jumps
