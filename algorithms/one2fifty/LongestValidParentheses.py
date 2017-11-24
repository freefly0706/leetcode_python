# -*- coding:utf-8 -*-
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        sLength = len(s)
        if sLength <= 1:
            return 0
        L = [0] * sLength
        if s[0] == '(' and s[1] == ')':
            L[1] = 2
        longest = L[1]
        for i in range(2, sLength):
            if s[i] == ')':
                left = i - 1 - L[i - 1]
                if L[i - 1] >= 2 and left >= 0 and s[left] == '(':
                    L[i] = L[i - 1] + 2
                    if left > 0:
                        L[i] += L[left - 1]
                elif s[i - 1] == '(':
                    L[i] = L[i - 2] + 2
                longest = max(longest, L[i])
        return longest
