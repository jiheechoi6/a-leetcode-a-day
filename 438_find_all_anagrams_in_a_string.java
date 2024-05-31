class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] freqs = new int[26];
        int[] freqp = new int[26];
        List<Integer> res = new ArrayList<Integer>();
        
        if(s.length() < p.length()) return res;

        // set up frequency for string p
        for(int i = 0; i < p.length(); i++){
            freqp[p.charAt(i) - 'a']++;
            freqs[s.charAt(i) - 'a']++;
        }

        int start = 0, end = p.length();
        if(Arrays.equals(freqs, freqp)) res.add(start);
        while(end < s.length()){
            freqs[s.charAt(start) - 'a']--;
            freqs[s.charAt(end) - 'a']++;

            if(Arrays.equals(freqs, freqp)) res.add(start+1);

            start++;
            end++;
        }
        
        return res;
    }
}
