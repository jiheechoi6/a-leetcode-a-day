class Solution {
public:
    int mySqrt(int x) {
        if(!x) return x;
        
        int left=1, right=x;
        while(left != right  && left != right-1){
            long mid = left + (right-left)/2;
            long sqr = mid*mid;
            if(sqr > x){
                right = mid;
            }else{
                left = mid;
            }
        }
        return left;
    }
};
