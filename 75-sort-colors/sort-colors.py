class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p1=nums[0]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    p1=nums[j]
                    nums[j]=nums[i]
                    nums[i]=p1
        return 



        