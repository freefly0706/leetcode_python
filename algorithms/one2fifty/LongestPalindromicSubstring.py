# -*- coding: UTF-8 -*-
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sLength = len(s)
        maxLength = 1
        startIndex = 0
        for i in range(sLength):
            p = i - 1
            q = i + 1
            while q < sLength and s[i] == s[q]:
                q += 1
            while p >= 0 and q < sLength and s[p] == s[q]:
                p -= 1
                q += 1
            if q - p - 1 > maxLength:
                startIndex = p + 1
                maxLength = q - p - 1
        return s[startIndex:startIndex + maxLength]
