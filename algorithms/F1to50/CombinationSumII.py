# -*-coding:utf-8 -*-
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        candidatesNum = len(candidates)
        res = []
        self.backTracking(res, [], 0, candidatesNum, candidates, target)
        return res

    def backTracking(self, res, combination, start, candidatesNum, candidates, target):
        if target == 0:
            res.append(combination.copy())
            return
        if target < 0:
            return
        for i in range(start, candidatesNum):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            combination.append(candidates[i])
            self.backTracking(res, combination, i + 1, candidatesNum, candidates, target - candidates[i])
            combination.pop()
