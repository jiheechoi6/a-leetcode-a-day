class Solution {
public:
    int climbStairs(int n) {
        if(n==1 || n==2)    return n;
        int twobefore=1, onebefore=2, ans=0;  // when n=1 and when n=2
        
        for(int i=3; i<=n; i++){
            ans = onebefore + twobefore;
            twobefore = onebefore;
            onebefore = ans;
        }
        return ans;
    }
};
