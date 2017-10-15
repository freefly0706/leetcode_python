# -*- coding: UTF-8 -*-
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        strlength = len(str)
        sign = 1
        result = 0
        for i in range(strlength):
            if str[i] != ' ':
                break
        if i == strlength:
            return 0
        if str[i] == '+' or str[i] == '-':
            sign = (-1 if (str[i] == '-') else 1)
            i += 1
        j = 1
        while i < strlength and '0' <= str[i] <= '9':
            result = result * 10 + int(str[i])
            i += 1
            if j > 10:
                break
            j += 1
        if result > 2147483647:
            return 2147483647 if sign == 1 else -2147483648
        return result * sign
