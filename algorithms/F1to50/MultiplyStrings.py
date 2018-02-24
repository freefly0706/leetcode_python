# -*-coding:utf-8 -*-
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1[0] == '0' or num2[0] == '0':
            return '0'
        num1_len, num2_len = len(num1), len(num2)
        res = [0] * (num1_len + num2_len)
        for i in range(num1_len - 1, -1, -1):
            for j in range(num2_len - 1, -1, -1):
                tmp = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                tmp += res[p2]
                res[p2] = tmp % 10
                res[p1] += tmp // 10
        index_of_zero = 0
        while res[index_of_zero] == 0:
            index_of_zero += 1
        return ''.join((str(i) for i in res[index_of_zero:num1_len + num2_len]))
