class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxh = 0
        
        while left < right:
            h = min(height[left], height[right]) * (right - left)
            maxh = max(maxh, h)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return maxh