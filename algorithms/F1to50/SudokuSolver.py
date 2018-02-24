# -*- coding:utf-8 -*-
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.backTracking(board, 0, 0, len(board))

    def backTracking(self, board, row, column, n):
        if column == n:
            return self.backTracking(board, row + 1, 0, n)
        if row == n:
            return True
        if board[row][column] == '.':
            for num in range(1, 10):
                if self.isValid(board, row, column, str(num), n):
                    board[row][column] = str(num)
                    if self.backTracking(board, row, column + 1, n):
                        return True
                    board[row][column] = '.'
            return False
        return self.backTracking(board, row, column + 1, n)

    def isValid(self, board, row, column, num, n):
        for i in range(n):
            if board[i][column] == num:
                return False
            if board[row][i] == num:
                return False
        startRow, startColumn = 3 * (row // 3), 3 * (column // 3)
        for i in range(1, 3):
            for j in range(1, 3):
                if board[startRow + (row + i) % 3][startColumn + (column + j) % 3] == num:
                    return False
        return True
