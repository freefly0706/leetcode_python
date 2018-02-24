# -*-coding:utf-8 -*-
class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.backTracking([0] * n, 0, n, 0)

    def backTracking(self, solution, row, n, totalNQueens):
        for col in range(n):
            if self.isValid(solution, row, col):
                solution[row] = col
                if row == n - 1:
                    totalNQueens += 1
                else:
                    totalNQueens = self.backTracking(solution, row + 1, n, totalNQueens)
        return totalNQueens

    def isValid(self, solution, row, col):
        if row > 0:
            for i in range(row):
                if solution[i] == col or abs(i - row) == abs(solution[i] - col):
                    return False
        return True
