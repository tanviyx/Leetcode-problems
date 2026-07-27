class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        x=nums[n-1]-1
        y=nums[n-2]-1
        return x*y

