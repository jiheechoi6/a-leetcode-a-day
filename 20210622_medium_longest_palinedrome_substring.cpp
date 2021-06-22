class Solution {
public:
    string longestPalindrome(string s) {
        bool mid = false;  // whether palindrome center is char or between chars
        int latest_mid = 0;
        int right_b = 0;
        int i = 0;
        string ans;
        hashmap<int, int> map;
        for(char elem: s){
            int right = (mid)? i+1:i;
            if(right_b > i){
                int mirror_i = 2*latest_mid-2i;
                if(mid) mirror_i++;
                right = i+map[mirror_i];
            }
            int left = mirror_i/2;
            
            int map_i = (mid)? 2*i+1:2*i;
            int cur_len = right-left+1;
            while(left>=0 && right<s.length()){
                if(s[left] == s[right]){
                    cur_len++;
                    if(right > right_b){
                        right_b = right;
                        latest_mid = map_i;
                    }
                }else{
                    break;
                }
            }
            
            if(mid) i++;
            mid = !mid;
        }
    }
};
