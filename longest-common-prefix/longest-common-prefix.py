class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Solution found on discussion
        # Smart solution. First find shortest string. 
        # Then loop through this string and compare with 
        # Strings array till you find the common prefix
        
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest
            
        