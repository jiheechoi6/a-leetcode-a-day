class Solution {
public:
    int reverse(int x) {
        int result = 0;
        // 2147483648
        while(abs(x)>0){
            int remainder = x%10;
            if((abs(result) >= 214748364 && remainder>=8) || (abs(result) > 214748364)) {
                return 0;
            }
            result = result*10 + remainder;
            x = (x-remainder)/10;
        }
        return result;
    }
};
