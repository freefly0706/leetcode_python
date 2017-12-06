# -*-coding:utf-8 -*-
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        previous = self.countAndSay(n - 1)
        length = len(previous)
        count = 1
        res = []
        for i in range(1, length):
            if previous[i - 1] == previous[i]:
                count += 1
            else:
                res.extend([str(count), previous[i - 1]])
                count = 1
        res.extend([str(count), previous[length - 1]])
        return ''.join(res)
