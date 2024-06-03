class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int sum = 0;
        target = Math.abs(target);
        
        for(int num: nums) sum += num;
        sum -= target;
        if(sum < 0 || (sum & 1) != 0) return 0;
        sum /=2;

        int[] dp = new int[sum+1];
        dp[0] = 1;

        for(int num: nums){
            for(int i = sum; i >= 0; i--){
                if(num <= i){
                    dp[i] = dp[i] + dp[i-num];
                }
            }
        }

        return dp[sum];
    }
}
