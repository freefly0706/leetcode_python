# -*-coding:utf-8 -*-
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        wordLen = len(words[0])
        wordsLen = len(words)
        wordsDict = {}
        for word in words:
            if word in wordsDict:
                wordsDict[word] += 1
            else:
                wordsDict[word] = 1
        for i in range(wordLen):
            count = 0
            startIndex = i
            tmp = {}
            for j in range(i, len(s) - wordLen + 1, wordLen):
                substringOut = s[j:j + wordLen]
                if substringOut in wordsDict:
                    if substringOut in tmp:
                        tmp[substringOut] += 1
                    else:
                        tmp[substringOut] = 1
                    if tmp[substringOut] > wordsDict[substringOut]:
                        while tmp[substringOut] > wordsDict[substringOut]:
                            substringIn = s[startIndex:startIndex + wordLen]
                            tmp[substringIn] -= 1
                            startIndex += wordLen
                            count -= 1
                    count += 1
                    if count == wordsLen:
                        res.append(startIndex)
                        substringIn = s[startIndex:startIndex + wordLen]
                        tmp[substringIn] -= 1
                        startIndex += wordLen
                        count -= 1
                else:
                    startIndex = j + wordLen
                    count = 0
                    tmp.clear()
        return res
