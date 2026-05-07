from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mer = []
        
        for i in range(len(nums1)):
            mer.append(nums1[i])

        for j in range(len(nums2)):
            mer.append(nums2[j])

        mer.sort()
        
        total = len(mer)

        if total % 2 == 0:
            return (mer[total//2 - 1] + mer[total//2]) / 2
        else:
            return mer[total//2]