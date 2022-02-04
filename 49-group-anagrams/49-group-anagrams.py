class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ### VERY CLEAN AND CONCISE SOLUTION ###
        
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return groups.values()