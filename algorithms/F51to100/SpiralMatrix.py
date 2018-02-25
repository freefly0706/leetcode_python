# -*-coding:utf-8 -*-
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if len(matrix) == 0:
            return res
        topLeftIndex = 0
        bottomRightRow = len(matrix) - 1
        bottomRightCol = len(matrix[0]) - 1
        while topLeftIndex <= bottomRightRow and topLeftIndex <= bottomRightCol:
            for col in range(topLeftIndex, bottomRightCol + 1):
                res.append(matrix[topLeftIndex][col])
            for row in range(topLeftIndex + 1, bottomRightRow + 1):
                res.append(matrix[row][bottomRightCol])
            if topLeftIndex < bottomRightRow and topLeftIndex < bottomRightCol:
                for col in range(bottomRightCol - 1, topLeftIndex - 1, -1):
                    res.append(matrix[bottomRightRow][col])
                for row in range(bottomRightRow - 1, topLeftIndex, -1):
                    res.append(matrix[row][topLeftIndex])
            topLeftIndex += 1
            bottomRightRow -= 1
            bottomRightCol -= 1
        return res
