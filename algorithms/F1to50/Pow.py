# -*-coding:utf-8 -*-
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        return self.binaryPow(x, n)

    def binaryPow(self, x, n):
        if n == 0:
            return 1.0
        if n == -1:
            return x
        left = self.binaryPow(x, n // 2)
        if n % 2 == 0:
            return left ** 2
        return left ** 2 * x
