class StringAlgorithm {
    public List<Integer> kmp(String s, String t){
        int m = s.length(), n = t.length();
        int []lps = new int[n];
        for(int i = 1; i<n; i++){
            int j = lps[i-1];
            while(j>0 && t.charAt(i)!=t.charAt(j)) j = lps[j-1];
            if(t.charAt(i) != t.charAt(j)) lps[i] = 0;
            else lps[i] = j+1;
        }
        
        int j = 0;
        List<Integer> res = new ArrayList<>();
        for(int i = 0; i<m; i++){
            while(j>0 && s.charAt(i) != t.charAt(j)) j = lps[j-1];
            if(s.charAt(i) == t.charAt(j)) j++;
            if(j == n){
                res.add(i-n+1); 
                j = lps[j-1];
            }
        }

        return res;
    }
}

class Solution {
    public long pow(long a, long b, int M){
        if(b == 0) return 1;
        if((b&1) == 0) return pow(a*a%M, b>>1, M);
        return a*pow(a*a%M, b>>1, M) % M;
    }

    public int numberOfWays(String s, String t, long k) {
        int n = s.length(), M = 1000000007;
        List<Integer> pos = new StringAlgorithm().kmp(s + s.substring(0, n-1), t);
        long []f_k = {0, 0};
        f_k[1] = (pow(n-1, k, M) + (k % 2 * 2 - 1) + M) % M * pow(n, M-2, M) % M;
        f_k[0] = (f_k[1] - (k % 2 * 2 - 1) + M) % M;
        int res = 0;
        for (Integer p: pos) {
            if (p == 0) res = (res + (int)f_k[0]) % M;
            else res = (res + (int)f_k[1]) % M;
        }
        return res;
    }
}
