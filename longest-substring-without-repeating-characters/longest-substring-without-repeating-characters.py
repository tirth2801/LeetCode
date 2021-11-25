class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # This is the solution which I cam up 
        # with and it was also there in the discussion
        # This uses the the Hash Map Approach
        
        # In ALGOEXPERT we are returning the longest substring and not the length
        
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            # Try to understand the second condition here
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
        