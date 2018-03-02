# -*-coding:utf-8 -*-
import numpy as np


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        spiralMatrix = np.zeros((n, n), dtype=np.int)
        topLeft = 0
        topRight = n - 1
        count = 1
        while topLeft <= topRight:
            dis = topRight - topLeft
            spiralMatrix[topLeft][topLeft:topRight + 1] = [num for num in range(count, count + dis + 1)]
            count += dis + 1  # 4
            spiralMatrix[:, topRight][topLeft + 1:topRight + 1] = [num for num in range(count, count + dis)]
            count += dis - 1  # 5
            spiralMatrix[topRight][topLeft:topRight] = [num for num in range(count + dis, count, -1)]
            count += dis  # 7
            spiralMatrix[:, topLeft][topLeft + 1:topRight] = [num for num in range(count + dis - 1, count, -1)]
            count += dis
            topLeft += 1
            topRight -= 1
        return spiralMatrix.tolist()
