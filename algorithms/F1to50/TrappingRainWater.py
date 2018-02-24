# -*- coding:utf-8 -*-
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        contain = 0
        left, right = 0, len(height) - 1
        while left < right:
            min_bound = min(height[left], height[right])
            while left < right and height[left] <= min_bound:
                contain += min_bound - height[left]
                left += 1
            while right > left and height[right] <= min_bound:
                contain += min_bound - height[right]
                right -= 1
        return contain
