# -*-coding:utf-8 -*-
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len, p_len = len(s), len(p)
        i, j, s_index, p_index = 0, 0, 0, -1
        while i < s_len:
            if j < p_len and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < p_len and p[j] == '*':
                j += 1
                s_index, p_index = i, j
            elif p_index != -1:
                s_index += 1
                i, j = s_index , p_index
            else:
                return False
        while j < p_len and p[j] == '*':
            j += 1
        return j == p_len
