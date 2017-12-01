# -*- coding:utf-8 -*-
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = len(board)
        round = 1
        grid = [[False for i in range(n)] for i in range(3)]
        for i in range(n):
            row = [False] * n
            column = [False] * n
            for j in range(n):
                if board[i][j] != '.':
                    rowIndex = int(board[i][j]) - 1
                    if row[rowIndex]:
                        return False
                    else:
                        row[rowIndex] = True
                    gridIndex = j // 3
                    if grid[gridIndex][rowIndex]:
                        return False
                    else:
                        grid[gridIndex][rowIndex] = True
                if board[j][i] != '.':
                    colIndex = int(board[j][i]) - 1
                    if column[colIndex]:
                        return False
                    else:
                        column[colIndex] = True
            if round == 3:
                round = 0
                grid = [[False for i in range(n)] for i in range(3)]
            round += 1
        return True
