from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        i = j = 0

        n = len(nums1)
        m = len(nums2)

        nums3 = []

        # Merge both arrays
        while i < n and j < m:

            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1

            else:
                nums3.append(nums2[j])
                j += 1

        # Remaining elements of nums1
        while i < n:
            nums3.append(nums1[i])
            i += 1

        # Remaining elements of nums2
        while j < m:
            nums3.append(nums2[j])
            j += 1

        total = n + m

        # Find median
        if total % 2 == 0:
            return (nums3[total // 2 - 1] + nums3[total // 2]) / 2

        else:
            return float(nums3[total // 2])