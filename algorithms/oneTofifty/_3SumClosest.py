# -*- coding: UTF-8 -*-
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        highBound = length
        closestMin = nums[0] + nums[1] + nums[2]
        closestMax = nums[length - 3] + nums[length - 2] + nums[length - 1]
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            low = i + 1
            high = highBound - 1
            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                if sum == target:
                    return target
                elif sum < target:
                    closestMin = max(closestMin, sum)
                    while low < high and nums[low + 1] == nums[low]:
                        low += 1
                    low += 1
                else:
                    if low == i + 1:
                        highBound -= 1
                    closestMax = min(closestMax, sum)
                    while low < high and nums[high - 1] == nums[high]:
                        high -= 1
                    high -= 1
        if (target - closestMin) > (closestMax - target):
            return closestMax
        else:
            return closestMin
