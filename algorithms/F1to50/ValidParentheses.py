# -*- coding: UTF-8 -*-
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parentheses = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c == '{' or c == '(' or c == '[':
                stack.append(c)
            else:
                if not stack or parentheses[stack.pop()] != c:
                    return False
        if stack:
            return False
        return True
