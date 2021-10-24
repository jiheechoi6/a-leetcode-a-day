class Solution {
public:
    int numSplits(string s) {
        int l_map[26] = {}, r_map[26] = {}, lcount = 1, rcount = 0;
        l_map[s[0]-'a'] += 1;
        s.erase(0, 1);
        int ans =0;
        for(auto ch:s){
            r_map[ch-'a'] += 1;
            if(r_map[ch-'a'] == 1){
                rcount += 1;
            }
        }
        
        for(int i=0; i< s.length(); i++){
            if(lcount == rcount) ans++;
            
            lcount += ++l_map[s[i]-'a'] ==1;
            rcount -= --r_map[s[i]-'a'] == 0;
        }
        
        return ans;
    }
};
