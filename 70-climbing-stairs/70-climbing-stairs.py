class Solution:
    def climbStairs(self, n: int) -> int:
        
        ### SOLUTION IS FROM DISCUSSION --- FIBONACCI METHOD ### 
        
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a