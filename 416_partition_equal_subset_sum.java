class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;

        for(int num: nums) sum += num;
        if((sum & 1) != 0) return false;

        sum /= 2;

        boolean[] dp = new boolean[sum+1];
        dp[0] = true;

        for(int num: nums){
            for(int i = sum; i > 0; i--){
                if(num <= i) dp[i] = dp[i] || dp[i-num];
            }
        }

        return dp[sum];
    }
}
