class Solution {
    public int numWays(String[] words, String target) {
        int mod = 1000000007;
        int wLen = words[0].length();
        int[][] charCnt = new int[wLen][26];

        for(int i = 0; i < words.length; i++){
            for(int j = 0; j< wLen; j++){
                charCnt[j][words[i].charAt(j) - 'a']++;
            }
        }

        int[][] dp = new int[wLen][target.length()];

        // dp[i][j] means number of variations forming target[0~j] using words position 0~i
        for(int i = 0; i< wLen; i++){
            for(int j = 0; j < target.length(); j++){
                if(i != 0) dp[i][j] += (dp[i-1][j] % mod); // don't put target[j] in column i
                if(j == 0) dp[i][j] += charCnt[i][target.charAt(j)-'a']; // put target
                int charCount = charCnt[i][target.charAt(j)-'a'];
                if(j != 0 && i != 0) dp[i][j] += (int)((long)charCount * dp[i-1][j-1] % mod); // put target[j] in column i
            }
        }

        return dp[wLen-1][target.length()-1] % mod;
    }
}
