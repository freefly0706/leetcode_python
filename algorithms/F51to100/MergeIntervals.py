# -*-coding:utf-8 -*-
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        res = []
        intervals.sort(key=lambda interval: interval.start)
        contInterval = intervals[0]
        for interval in intervals:
            if interval.start <= contInterval.end:
                contInterval.end = max(interval.end, contInterval.end)
            else:
                res.append(contInterval)
                contInterval = interval
        res.append(contInterval)
        return res
