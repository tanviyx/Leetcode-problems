from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            find=target-nums[i]
            if find in nums and nums.index(find)!=i:
                return [i,nums.index(find)]
            