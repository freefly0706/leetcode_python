# -*- coding: UTF-8 -*-
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        shortest_str_index = 0
        shortest_len = len(strs[0])
        for i in range(1, len(strs)):
            if len(strs[i]) < shortest_len:
                shortest_len = len(strs[i])
                shortest_str_index = i
        res = strs[shortest_str_index]
        while True:
            i = 0
            while i < len(strs):
                if strs[i][:shortest_len] != res[:shortest_len]:
                    shortest_len -= 1
                    continue
                i += 1
            return res[:shortest_len]
