# -*- coding: UTF-8 -*-
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        base_string = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        base_int = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for i in range(len(base_string)):
            while num >= base_int[i]:
                res += base_string[i]
                num -= base_int[i]
        return res
