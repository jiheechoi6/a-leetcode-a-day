class Solution {
public:
    string longestPalindrome(string s) {
        if(s.length() <= 1) return s;
        
        int strlen = s.length();
        int maxlen = 0, final_l=0;
        for(int i=0; i<strlen;){
            int l = i, r=i;
            
            while(r<strlen-1 && s[r]==s[r+1]){  // skip duplicates
                r++;
            }
            i = r+1;
            
            while(l>0 && r<strlen-1 && s[l-1]==s[r+1]){
                l--;
                r++;
            }
            
            if(maxlen < (r-l+1)){
                maxlen = r-l+1;
                final_l = l;
            }
        }
        return s.substr(final_l, maxlen);
    }
};
