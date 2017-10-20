# -*- coding: UTF-8 -*-
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        high_bound = len(nums)
        for i in range(high_bound - 3):
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[high_bound - 1] + nums[high_bound - 2] + nums[high_bound - 3] < target:
                continue
            if i > 0 and (nums[i] == nums[i - 1]):
                continue
            for j in range(i + 1, high_bound - 2):
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[high_bound - 1] + nums[high_bound - 2] < target:
                    continue
                if j > i + 1 and (nums[j] == nums[j - 1]):
                    continue
                low = j + 1
                high = high_bound - 1
                while low < high:
                    sums = nums[i] + nums[j] + nums[low] + nums[high]
                    if sums == target:
                        res.append([nums[i], nums[j], nums[low], nums[high]])
                        while low < high and nums[low + 1] == nums[low]:
                            low += 1
                        while low < high and nums[high - 1] == nums[high]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif sums < target:
                        low += 1
                    else:
                        if low == i + 2:
                            high_bound -= 1
                        high -= 1
        return res
