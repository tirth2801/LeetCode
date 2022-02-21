class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        ### SLIDING WINDOW PATTERN
        
        sum = 0
        for i in range(0, k):
            sum += arr[i]
        average = sum / k
        
        numSubArrays = 0
        
        if average >= threshold:
            numSubArrays += 1
        
        
        for i in range(k, len(arr)):
            sum -= arr[i - k]
            sum += arr[i]
            currAverage = sum / k
            if currAverage >= threshold:
                numSubArrays += 1
        return numSubArrays