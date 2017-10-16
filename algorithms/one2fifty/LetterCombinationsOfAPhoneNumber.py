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
        lastDigitLetterCombi = digitCorString[digits[digitsLength - 1]]
        for i in range(len(lastDigitLetterCombi)):
            res.append(lastDigitLetterCombi[i])
        for i in range(digitsLength - 2, -1, -1):
            letterCombi = digitCorString[digits[i]]
            resLength = len(res)
            for j in range(resLength):
                temp = res.pop(0)
                for c in letterCombi:
                    res.append(c + temp)
        return res