from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index1, index2 = -1, -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    index1 = i
                    index2 = j
                    return [index1, index2]   