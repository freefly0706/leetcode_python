# -*- coding:utf-8 -*-
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        needleLength = len(needle)
        for i in range(len(haystack) - needleLength + 1):
            if haystack[i] == needle[0]:
                if haystack[i:i + needleLength] == needle:
                    return i
        return -1
