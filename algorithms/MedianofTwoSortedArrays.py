# -*- coding: UTF-8 -*-
import sys


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        k = length // 2
        if length % 2 != 0:
            return self.getKthSmall(nums1, 0, nums2, 0, k + 1)
        return (self.getKthSmall(nums1, 0, nums2, 0, k) + self.getKthSmall(nums1, 0, nums2, 0, k + 1)) / 2

    def getKthSmall(self, nums1, start1, nums2, start2, k):
        if start1 > len(nums1) - 1:
            return nums2[start2 + k - 1]
        if start2 > len(nums2) - 1:
            return nums1[start1 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])
        mid1 = mid2 = sys.maxsize
        if start1 + k // 2 - 1 < len(nums1):
            mid1 = nums1[start1 + k // 2 - 1]
        if start2 + k // 2 - 1 < len(nums2):
            mid2 = nums2[start2 + k // 2 - 1]
        if mid1 < mid2:
            return self.getKthSmall(nums1, start1 + k // 2, nums2, start2, k - k // 2)
        return self.getKthSmall(nums1, start1, nums2, start2 + k // 2, k - k // 2)
