# -*-coding:utf-8 -*-
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        solutions = []
        self.backTracking(solutions, [0] * n, 0, n)
        for solution in solutions:
            tmp = []
            board = [['.' for i in range(n)] for i in range(n)]
            for i in range(n):
                board[i][solution[i]] = 'Q'
                tmp.append(''.join(board[i]))
            res.append(tmp)
        return res

    def backTracking(self, solutions, solution, row, n):
        for col in range(n):
            if self.isValid(row, col, solution):
                solution[row] = col
                if row == n - 1:
                    solutions.append(solution.copy())
                else:
                    self.backTracking(solutions, solution, row + 1, n)

    def isValid(self, row, col, solution):
        if row > 0:
            for i in range(row):
                if solution[i] == col or abs(i - row) == abs(solution[i] - col):
                    return False
        return True
