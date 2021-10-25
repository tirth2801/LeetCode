class Solution {
    public int rob(int[] nums) {
        int current = 0;
        int previous = 0;
        int temporary;
        for(int n: nums){
            temporary = current;
            current = Math.max(previous + n, current);
            previous = temporary;
        }
        return current;
    }
}