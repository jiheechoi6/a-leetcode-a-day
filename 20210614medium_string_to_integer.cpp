class Solution {
public:
    int myAtoi(string s) {
        bool step1 = true;
        bool sign_checked = false;
        bool step2 = false;
        bool step3 = false;

        int sign = 1;
        int answer = 0;
        for(char c: s){
            if(step1 && c != ' '){  // check whitespace
                step1 = false;
                step2 = true;
            }
            if(step2){  // check sign
                if(c == '-' || c=='+'){
                    if(sign_checked){
                        return 0;
                    }
                    if(c == '-'){
                        sign = -1;
                    }
                    sign_checked = true;
                }else{
                    step2 = false;
                    step3 = true;
                }
            }
            if(step3 ){  // get int
                if(48<=int(c) && int(c)<=57){
                    int check = (sign > 0)? 1:0;
                    if(abs(answer) >214748364 || (int(c)-48+check>8 && abs(answer)==214748364)){
                        cout << sign;
                        if(sign==1)    return 2147483647;
                        return -2147483648;
                    }
                    int num = int(c) -48;
                    answer = answer*10 + sign*num;
                }else{
                    return answer;
                }
            }
        }
        return answer;
    }
};
