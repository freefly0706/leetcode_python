# -*- coding: UTF-8 -*-
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digitsLength = len(digits)
        res = []
        if digitsLength == 0:
            return res
        digitCorString = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv",
                          '9': "wxyz"}

        def backTracking(combination, index):
            if index == digitsLength:
                res.append(combination)
                return
            char2int = digits[index]
            for c in digitCorString[char2int]:
                backTracking(combination + c, index + 1)

        backTracking('', 0)
        return res
