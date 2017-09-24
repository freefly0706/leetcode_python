# -*- coding: UTF-8 -*-
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_value = 0
        while left < right:
            min_bound = min(height[left], height[right])
            max_value = max(max_value, min_bound * (right - left))
            while left < len(height) and height[left] <= min_bound:
                left += 1
            while right > 0 and height[right] <= min_bound:
                right -= 1
        return max_value
