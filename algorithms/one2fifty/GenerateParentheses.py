# -*- coding:utf-8 -*-
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        Solution().backTracking('', n, 0, 0, res)
        return res

    def backTracking(self, pair, n, left, right, res):
        if right == n:
            res.append(pair)
            return
        if left < n:
            Solution().backTracking(pair + '(', n, left + 1, right, res)
        if right < left:
            Solution().backTracking(pair + ')', n, left, right + 1, res)
