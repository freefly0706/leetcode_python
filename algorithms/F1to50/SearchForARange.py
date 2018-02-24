# -*-coding:utf-8 -*-
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if low > high:
            return res
        leftHigh, rightLow = mid - 1, mid + 1
        while low <= leftHigh:
            mid = (low + leftHigh) // 2
            if nums[mid] != target:
                low = mid + 1
            else:
                leftHigh = mid - 1
        res[0] = low
        while rightLow <= high:
            mid = (rightLow + high) // 2
            if nums[mid] != target:
                high = mid - 1
            else:
                rightLow = mid + 1
        res[1] = high
        return res
