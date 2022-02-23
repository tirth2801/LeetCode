class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        ### SMART SOLUTION FROM DISCUSSION
        ### EASY TO UNDERSTAND...
        
        hmap = {} ## Hashmap
        res = [] ## Result array
        
        for idx, groupSize in enumerate(groupSizes):
            if groupSize in hmap:
                hmap[groupSize].append(idx)
            else:
                hmap[groupSize] = [idx]
                
            
            ### -----------SMART STUFF--------------- ###
            if len(hmap[groupSize]) == groupSize:
                res += [hmap[groupSize]]
                hmap[groupSize] = []
            ### ------------------------------------ ###
        
        
        return res