class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        int[] dp = new int[days.length+1];
        dp[0] = 0;

        for(int i = 1; i <= days.length; i++){
            int pass1 = dp[i-1] + costs[0];

            int lastUncovered = i-1;
            while(lastUncovered >= 0 && (days[i-1] - days[lastUncovered]) < 7) lastUncovered--;

            int pass7 = costs[1] + dp[lastUncovered+1];

            lastUncovered = i-1;
            while(lastUncovered >= 0 && (days[i-1] - days[lastUncovered]) < 30) lastUncovered--;
            int pass30 = costs[2] + dp[lastUncovered+1];

            dp[i] = Math.min(pass1, Math.min(pass7, pass30));
        }

        return dp[days.length];
    }
}
