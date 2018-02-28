# -*-coding:utf-8 -*-
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        length = len(intervals)
        i = 0
        while i < length and intervals[i].end < newInterval.start:
            res.append(intervals[i])
            i += 1
        if i < length:
            newInterval.start = min(newInterval.start, intervals[i].start)
            while i < length and intervals[i].start <= newInterval.end:
                i += 1
            if i > 0:
                newInterval.end = max(newInterval.end, intervals[i - 1].end)
        res.append(newInterval)
        res.extend(intervals[i:length])
        return res
