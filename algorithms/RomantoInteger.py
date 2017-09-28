# -*- coding: UTF-8 -*-
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        base = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        while i < len(s) - 1:
            if base[s[i]] < base[s[i + 1]]:
                res += base[s[i + 1]] - base[s[i]]
                i += 2
            else:
                res += base[s[i]]
                i += 1
        if i == len(s) - 1:
            res += base[s[i]]
        return res
