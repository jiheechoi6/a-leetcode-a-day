class Solution {
public:
    string longestPalindrome(string s) {
        int latest_mid = 0;
        int right_b = 0;
        string ans = s.substr(0, 1);
        int max_len = 1;
        vector<int> map;
        vector<string> palindromes;
        int map_len = s.length()*2 -1;
        
        for(int i=0; i<map_len; i++){
            int right = (i%2 == 0)? i+2: i+1;
            string cur_palindrome = (i%2 == 0)? s.substr(i/2, 1): string();
            
            if(right_b > i){
                int mirror_i = 2*latest_mid-i;
                right = i+map[mirror_i];
                cur_palindrome = palindromes[mirror_i];
            }
            int left = 2*i-right;
            
            while(left>=0 && right<map_len){
                if(right%2 == 1){
                    left--;
                    right++;
                    continue;
                }
                if(s[left/2] != s[right/2]) break;
                if(s[left/2] == s[right/2]){
                    cur_palindrome = s[left/2] + cur_palindrome + s[left/2];
                    if(right > right_b){
                        right_b = right;
                        latest_mid = i;
                    }
                }     
                left--;
                right++;
            }
            
            int cur_len = cur_palindrome.length();
            if(max_len < cur_len){
                max_len = cur_len;
                ans = cur_palindrome;
            }
            map.push_back(right-i);
            palindromes.push_back(cur_palindrome);
        }
        return ans;
    }
};
