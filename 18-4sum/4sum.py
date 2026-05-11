class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        
        ans = []
        s = set()
        
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                
                left = j + 1
                right = n - 1
                
                while left < right:
                    
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        
                        quad = (nums[i], nums[j], nums[left], nums[right])
                        
                        if quad not in s:
                            ans.append(list(quad))
                            s.add(quad)
                        
                        left += 1
                    
                    elif total < target:
                        left += 1
                    
                    else:
                        right -= 1
        
        return ans
