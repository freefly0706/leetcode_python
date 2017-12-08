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
            self.backTracking(pair + '(', n, left + 1, right, res)
        if right < left:
            self.backTracking(pair + ')', n, left, right + 1, res)
