# -*- coding: UTF-8 -*-
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        maxLength = 0
        q = 0
        temp = {}
        length = len(s)
        for i in range(length):
            if s[i] in temp.keys():
                maxLength = max(count, maxLength)
                q = max(q, temp[s[i]])
                count = i - q
            count += 1
            temp[s[i]] = i + 1
        maxLength = max(count, maxLength)
        return maxLength
