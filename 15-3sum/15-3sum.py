class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # FOUND in Discussion easy to understand
        # Smart approach using sort and 2 pointers
        
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            
            # Disregarding equal values
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Setting to negative because we have to 
            # find the sum of remaining two numbers
            target = nums[i] * -1
            
            # Setting new pointer and looping through
            left, right = i + 1, N - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    
                    # This while loop finds the next value not equal 
                    # to previous value
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return result