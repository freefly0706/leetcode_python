# -*- coding: UTF-8 -*-
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        M = [([False] * (len(p) + 1)) for i in range(len(s) + 1)]
        M[0][0] = True
        for i in range(len(p)):
            if p[i] == '*' and M[0][i - 1]:
                M[0][i + 1] = True
        for i in range(len(s)):
            for j in range(len(p)):
                if s[i] == p[j] or p[j] == '.':
                    M[i + 1][j + 1] = M[i][j]
                elif p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        M[i + 1][j + 1] = M[i + 1][j - 1]
                    else:
                        M[i + 1][j + 1] = M[i + 1][j] or M[i + 1][j - 1] or M[i][j + 1]
        return M[len(s)][len(p)]
