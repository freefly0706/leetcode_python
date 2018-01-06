# -*-coding:utf-8 -*-
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        dim = len(matrix)
        for i in range(1, dim):
            for j in range(0, i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        for j in range(dim // 2):
            for i in range(dim):
                back = dim - 1 - j
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][back]
                matrix[i][back] = tmp
