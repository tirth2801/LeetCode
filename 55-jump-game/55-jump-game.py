class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        ### GOING FORWARD ###
        
        # m = 0
        # for i, n in enumerate(nums):
        #     if i > m:
        #         return False
        #     m = max(m, i+n)
        # return True
    
    
        ### GOING BACKWARDS ###
        
        goal = len(nums) - 1
        for i in reversed(range(len(nums))):
        # for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal

    