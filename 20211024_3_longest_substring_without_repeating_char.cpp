class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> dict(256, -1);
        int mxlen = 0, start = -1;
        for(int i=0; i<s.length(); i++){
            int val = s[i];
            if(dict[val]>start){
                start = dict[val];
            }
        
            mxlen = max(mxlen, i-start);
            dict[val] = i;
        }
        return mxlen;
    }
};
