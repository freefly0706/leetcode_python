# -*-coding:utf-8 -*-
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidatesNum = len(candidates)
        res = []
        self.backTracking(res, [], 0, candidatesNum, candidates, target)
        return res

    def backTracking(self, res, combination, start, candidatesNum, candidates, target):
        if start == candidatesNum or target <= 0:
            if target == 0:
                res.append(combination.copy())
            return
        combination.append(candidates[start])
        self.backTracking(res, combination, start, candidatesNum, candidates, target - candidates[start])

        combination.pop()
        self.backTracking(res, combination, start + 1, candidatesNum, candidates, target)
