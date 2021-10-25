class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = Integer.MIN_VALUE;
        int sum = 0;
        
        for(int num: nums) {
            if(sum < 0){
                sum = num;
            }
            else{
                sum += num;
            }
            
            maxSum = Math.max(maxSum, sum);
        }
        return maxSum;
    }
}