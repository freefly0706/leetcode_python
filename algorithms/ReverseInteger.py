# -*- coding: UTF-8 -*-
import sys


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = x
        if y < 0:
            y = -y
        res = 0
        while y != 0:
            res = res * 10 + y % 10
            y //= 10
        if res > 2 ** 31 - 1:
            return 0
        if x < 0:
            return -res
        return res
