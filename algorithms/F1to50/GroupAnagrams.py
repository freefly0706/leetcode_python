# -*-coding:utf-8 -*-
import collections


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicts = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in dicts:
                dicts[key].append(s)
            else:
                dicts[key] = [s]
        return list(dicts.values())

    '''
    In Java, the hashTable representation of our count will be a string delimited with '#' characters.
    For example, abbccc will be #1#2#3#0#0#0...#0 where there are 26 entries total.
    In python, the representation will be a tuple of the counts.
    For example, abbccc will be (1, 2, 3, 0, 0, ..., 0), where again there are 26 entries total.
    '''
    # def groupAnagrams(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: List[List[str]]
    #     """
    #     dicts = collections.defaultdict(list)
    #     for s in strs:
    #         count = [0] * 26
    #         for ch in s:
    #             count[ord(ch) - ord('a')] += 1
    #         dicts[tuple(count)].append(s)
    #     return list(dicts.values())
