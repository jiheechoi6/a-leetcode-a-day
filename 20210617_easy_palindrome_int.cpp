class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0){
            return false;
        }
        
        long long reverse = 0;
        long long track = x;
        while(track>0){
            reverse = reverse*10 + track%10;
            track = track/10;
        }

        return reverse ==x? true: false;
    }
};
