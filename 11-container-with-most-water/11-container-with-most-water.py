class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Very Smart approach found on Discussion
        
        # Two pointer approach coming inside from 
        # the two extreme indices
        
        # Time - O(n) | Space - O(1)
        
        MAX = 0 
        x = len(height) - 1
        y = 0
        while x != y:
            if height[x] > height[y]:
                area = height[y] * (x - y)
                y += 1
            else:
                area = height[x] * (x - y)
                x -= 1
            MAX = max(MAX, area)
        return MAX