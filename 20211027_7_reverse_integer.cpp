class Solution {
public:
    int reverse(int x) {
        long long res = 0;
        while(x){
            res = res*10+x%10;
            x /=10;
        }
        
        if(res<INT_MAX && res>INT_MIN){
            return res;
        }else{
            return 0;
        }
        return (res>INT_MAX || res<INT_MIN)? 0:res;
    }
};
