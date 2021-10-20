class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ###  FROM DISCUSSION  ###
        
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i
        
    
            
        