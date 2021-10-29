class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string pref = "";
        
        for(int i; i<strs[0].length(); i++){
            for(int j=1; j<strs.size(); j++){
                if(i>=strs[j].length() || strs[0][i] != strs[j][i]){
                    return pref;
                }
            }
            pref += strs[0][i];
        }
        
        return pref;
    }
};
