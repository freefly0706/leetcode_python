# -*- coding:utf-8 -*-
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needleLength = len(needle)
        if not needleLength:
            return 0
        haystackLength = len(haystack)
        for i in range(needleLength - 1, haystackLength):
            if haystack[i] == needle[needleLength - 1]:
                if haystack[i + 1 - needleLength:i + 1] == needle:
                    return i + 1 - needleLength
        return -1
