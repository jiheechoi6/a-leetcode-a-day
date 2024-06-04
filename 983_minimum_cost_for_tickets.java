class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        int[] dp = new int[days.length];
        dp[0] = costs[0];

        for(int i = 1; i < days.length; i++){
            int cost1 = dp[i-1] + costs[0];

            int lastUncovered = i-1;
            while(lastUncovered != -1 && (days[i] - days[lastUncovered]) < 7) lastUncovered--;
            int cost7 = costs[1];
            if(lastUncovered != -1) cost7 += dp[lastUncovered]; 
            
            lastUncovered = i-1;
            while(lastUncovered != -1 && (days[i] - days[lastUncovered]) < 30) lastUncovered--;
            int cost30 = costs[2];
            if(lastUncovered != -1) cost30 += dp[lastUncovered]; 

            dp[i] = Math.min(cost1, Math.min(cost7, cost30));
        }

        return dp[days.length - 1];
    }
}
