// KPM solution
class Solution {
    public int strStr(String haystack, String needle) {
        int m = haystack.length(), n = needle.length();
        int []lps = new int[n];
        for(int i = 1; i< n; i++){
            int j = lps[i-1];
            while(j>0 && needle.charAt(i) != needle.charAt(j)) j = lps[j-1];
            if(needle.charAt(i) != needle.charAt(j)) lps[i] = 0;
            else lps[i] = j+1;
        }

        int j = 0;
        for( int i = 0; i<m; i++){
            while (j>0 && haystack.charAt(i) != needle.charAt(j)) j = lps[j-1];
            if(haystack.charAt(i) == needle.charAt(j)) j++;
            if(j == n) return i-n+1;
        }
        return -1;
    }
}
