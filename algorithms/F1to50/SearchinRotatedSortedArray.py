# -*- coding:utf-8 -*-
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if nums[low] > nums[mid] and nums[high] < target:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[high] < nums[mid] and nums[low] > target:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
