class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        ex=0
        for i in range(len(nums)):
            if nums[i]!=nums[i-1] or i-1==-1 :
                nums[k]=nums[i]
                k+=1
                ex=1
            elif (nums[i]==nums[i-1] and ex==1):
                nums[k]=nums[i]
                k+=1
                ex=0
            
        return k
