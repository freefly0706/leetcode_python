# -*-coding:utf-8 -*-
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if not divisor or (dividend == -2 ** 31 and divisor == -1):
            return 2 ** 31 - 1
        sign = (dividend < 0) is (divisor < 0)
        res = 0
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            temp, mul = divisor, 1
            while dividend >= temp << 1:
                temp <<= 1
                mul <<= 1
            dividend -= temp
            res += mul
        return res if sign else -res
