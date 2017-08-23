# -*- coding: UTF-8 -*-
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        half_of_x = 0
        while x > half_of_x:
            half_of_x = half_of_x * 10 + x % 10
            x /= 10
        return x == half_of_x or x == half_of_x / 10
